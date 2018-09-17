import datetime

level0 = frozenset(['INDI', 'FAM', 'NOTE'])
level1 = frozenset(['NAME', 'SEX', 'FAMC', 'FAMS', 'HUSB', 'WIFE', 'CHIL'])
level2 = frozenset(['DATE'])

validTags = [level0, level1, level2]
validLevels = frozenset([0, 1, 2])

validTagsNoArgs = [frozenset(['HEAD', 'TRLR']), frozenset(['BIRT', 'DEAT', 'MARR', 'DIV'])]
validLevelsNoArgs = frozenset([0, 1])

gedcomFileName = 'test.ged'
gedcomFile = open(gedcomFileName, 'r')
validatedFile = []

LEVEL = 0
TAG = 1
ARG = 2

def validateFile(gedcomFile):
    validatedFile = []
    
    for rawLine in gedcomFile:
        line = rawLine.strip().split(' ', 2)
        validatedLine = None
        
        if len(line) >= 2 and len(line) <= 3:
            try:
                level = int(line[0])
                if len(line) == 2:
                    tag = line[1]
                    arguments = None
                else:
                    if line[2] == 'INDI' or line[2] == 'FAM':
                        tag = line[2]
                        arguments = line[1]
                    else:
                        tag = line[1]
                        arguments = line[2]
                        if tag == 'INDI' or tag == 'FAM':
                            raise ValueError
                
                if level in validLevelsNoArgs and tag in validTagsNoArgs[level] and not arguments:
                    validatedLine = [level, tag, arguments]
                elif level in validLevels and tag in validTags[level]:
                    if tag == 'DATE':
                        datetime.datetime.strptime(arguments, '%d %b %Y')
                        validatedLine = [level, tag, arguments]
                    else:
                        validatedLine = [level, tag, arguments]
                
                if validatedLine:
                    validatedFile.append(validatedLine)
                else:
                    print('Invalid: %s' % rawLine.strip())
            except ValueError:
                print('Invalid: %s' % rawLine.strip())
        else:
            print('Invalid: %s' % rawLine.strip())
    
    return validatedFile

def parseFile(validatedFile):
    individualTable = []
    familyTable = []
    fileLength = len(validatedFile)
    lineNum = 0
    individual = {'INDI': None, 'NAME': None, 'SEX': None, 'BIRT': None, 'DEAT': None, 'FAMC': None, 'FAMS': []}
    family = {'FAM': None, 'MARR': None, 'DIV': None, 'HUSB': None, 'WIFE': None, 'CHIL': []}

    while lineNum < fileLength:
        line = validatedFile[lineNum]
        if line[TAG] == 'INDI':
            individual['INDI'] = line[ARG]
            nextLineNum = lineNum + 1
            nextLine = validatedFile[nextLineNum]
            while nextLineNum < fileLength and nextLine[TAG] != 'INDI' and nextLine[TAG] != 'FAM':
                if nextLine[TAG] == 'BIRT' or nextLine[TAG] == 'DEAT':
                    nextLineNum += 1
                    individual[nextLine[TAG]] = validatedFile[nextLineNum][ARG]
                elif nextLine[TAG] != 'NOTE' and nextLine[TAG] != 'HEAD' and nextLine[TAG] != 'TRLR':
                    if nextLine[TAG] == 'FAMS' or nextLine[TAG] == 'FAMC':
                        individual[nextLine[TAG]].append(nextLine[ARG])
                    else:
                        individual[nextLine[TAG]] = nextLine[ARG]

                nextLineNum += 1
                lineNum = nextLineNum
                if nextLineNum < fileLength:
                    nextLine = validatedFile[nextLineNum]
            if lineNum < fileLength:
                line = validatedFile[lineNum]
        elif line[TAG] == 'FAM':
            family['FAM'] = line[ARG]
            nextLineNum = lineNum + 1
            nextLine = validatedFile[nextLineNum]
            while nextLineNum < fileLength and nextLine[TAG] != 'INDI' and nextLine[TAG] != 'FAM':
                if nextLine[TAG] == 'MARR' or nextLine[TAG] == 'DIV':
                    nextLineNum += 1
                    family[nextLine[TAG]] = validatedFile[nextLineNum][ARG]
                elif nextLine[TAG] != 'NOTE' and nextLine[TAG] != 'HEAD' and nextLine[TAG] != 'TRLR':
                    if nextLine[TAG] == 'CHIL':
                        family['CHIL'].append(nextLine[ARG])
                    else:
                        family[nextLine[TAG]] = nextLine[ARG]

                nextLineNum += 1

                lineNum = nextLineNum
                if nextLineNum < fileLength:
                    nextLine = validatedFile[nextLineNum]
        else:
            lineNum += 1
        if individual['INDI']:
            individualTable.append(individual)
            individual = {'INDI': None, 'NAME': None, 'SEX': None, 'BIRT': None, 'DEAT': None, 'FAMC': [], 'FAMS': []}

        if family['FAM']:
            familyTable.append(family)
            family = {'FAM': None, 'MARR': None, 'DIV': None, 'HUSB': None, 'WIFE': None, 'CHIL': []}
    return [individualTable, familyTable]

def buildIndividualCollection(individualTable):
    individualCol = []

    for individual in individualTable:
        newIndividual = {'ID': None, 'Name': None, 'Gender': None, 'Birthday': None, 'Age': None, 'Alive': None, 'Death': None, 'Child': None, 'Spouse': []}
        
        newIndividual['ID'] = individual['INDI']
        newIndividual['Name'] = individual['NAME']
        newIndividual['Gender'] = individual['SEX']
        newIndividual['Child'] = individual['FAMC']
        newIndividual['Spouse'] = individual['FAMS']
        
        birthday = datetime.datetime.strptime(individual['BIRT'], '%d %b %Y')
        newIndividual['Birthday'] = birthday.strftime('%Y-%m-%d')
        date = datetime.date.today()

        if individual['DEAT'] == None:
            newIndividual['Alive'] = 'True'
        else:
            newIndividual['Alive'] = 'False'
            date = datetime.datetime.strptime(individual['DEAT'], '%d %b %Y')
            newIndividual['Death'] = date.strftime('%Y-%m-%d')
        
        newIndividual['Age'] = date.year - birthday.year - ((date.month, date.day) < (birthday.month, birthday.day))
        
        individualCol.append(newIndividual)
    return individualCol

def buildFamilyCollection(familyTable, individualCol):
    familyCol = []

    for family in familyTable:
        newFamily = {'ID': None, 'Married': None, 'Divorced': None, 'Husband ID': None, 'Husband Name': None, 'Wife ID': None, 'Wife Name': None, 'Children': []}

        newFamily['ID'] = family['FAM']
        newFamily['Married'] = datetime.datetime.strptime(family['MARR'], '%d %b %Y').strftime('%Y-%m-%d')
        if family['DIV']:
            newFamily['Divorced'] = datetime.datetime.strptime(family['DIV'], '%d %b %Y').strftime('%Y-%m-%d')

        newFamily['Husband ID'] = family['HUSB']
        newFamily['Wife ID'] = family['WIFE']
        newFamily['Children'] = family['CHIL']

        for individual in individualCol:
            if individual['ID'] == family['HUSB']:
                newFamily['Husband Name'] = individual['Name']
            if individual['ID'] == family['WIFE']:
                newFamily['Wife Name'] = individual['Name']
        familyCol.append(newFamily)
    
    return familyCol

validatedFile = validateFile(gedcomFile)
tables = parseFile(validatedFile)
individualCol = buildIndividualCollection(tables[0])
familyCol = buildFamilyCollection(tables[1], individualCol)

for i in individualCol:
    print(i)

for f in familyCol:
    print(f)
