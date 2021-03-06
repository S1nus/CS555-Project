import datetime
from prettytable import PrettyTable

level0 = frozenset(['INDI', 'FAM', 'NOTE'])
level1 = frozenset(['NAME', 'SEX', 'FAMC', 'FAMS', 'HUSB', 'WIFE', 'CHIL'])
level2 = frozenset(['DATE'])

validTags = [level0, level1, level2]
validLevels = frozenset([0, 1, 2])

validTagsNoArgs = [frozenset(['HEAD', 'TRLR']), frozenset(['BIRT', 'DEAT', 'MARR', 'DIV'])]
validLevelsNoArgs = frozenset([0, 1])

LEVEL = 0
TAG = 1
ARG = 2

exit = False

def readFile():
    gedcomFile = None
    gedcomFileName = input('Please enter the name of your GEDCOM file:\n')

    while gedcomFile == None:
        try:
            gedcomFile = open('../gedcom_files/%s' % gedcomFileName, 'r')
        except FileNotFoundError:
            gedcomFileName = input('File \"%s\" not found in gedcom_files folder. Please re-enter the name of your GEDCOM file:\n' % gedcomFileName)

    return gedcomFile

def validateFile(gedcomFile):
    validatedFile = []
    lineNum = 0

    for rawLine in gedcomFile:
        lineNum += 1
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
                    validatedFile.append((validatedLine, lineNum))
                else:
                    print('%s:Invalid: %s' % (lineNum, rawLine.strip()))
            except ValueError:
                print('%s:Invalid: %s' % (lineNum, rawLine.strip()))
        else:
            print('%s:Invalid: %s' % (lineNum, rawLine.strip()))
    
    return validatedFile

def parseFile(validatedFile):
    individualTable = []
    familyTable = []
    fileLength = len(validatedFile)
    lineNum = 0
    individual = {'INDI': None, 'NAME': None, 'SEX': None, 'BIRT': None, 'DEAT': None, 'FAMC': [], 'FAMS': [], 'lines': {}}
    family = {'FAM': None, 'MARR': None, 'DIV': None, 'HUSB': None, 'WIFE': None, 'CHIL': [], 'lines': {}}

    indiList = []
    famList = []

    while lineNum < fileLength:
        lineNumDict = {}
        line = validatedFile[lineNum][0]
        fileLineNum = validatedFile[lineNum][1]
        if line[TAG] == 'INDI':
            individual['INDI'] = line[ARG]
            individual['lines'][individual['INDI'] + line[TAG]] = fileLineNum
            nextLineNum = lineNum + 1
            nextLine = validatedFile[nextLineNum][0]
            nextFileLineNum = validatedFile[nextLineNum][1]
            while nextLineNum < fileLength and nextLine[TAG] != 'INDI' and nextLine[TAG] != 'FAM':
                if nextLine[TAG] == 'BIRT' or nextLine[TAG] == 'DEAT':
                    nextLineNum += 1
                    nextFileLineNum = validatedFile[nextLineNum][1]
                    individual[nextLine[TAG]] = validatedFile[nextLineNum][0][ARG]
                    individual['lines'][individual['INDI'] + nextLine[TAG]] = nextFileLineNum
                elif nextLine[TAG] != 'NOTE' and nextLine[TAG] != 'HEAD' and nextLine[TAG] != 'TRLR':
                    if nextLine[TAG] == 'FAMS' or nextLine[TAG] == 'FAMC':
                        individual[nextLine[TAG]].append(nextLine[ARG])
                        individual['lines'][nextLine[ARG] + nextLine[TAG]] = nextFileLineNum
                    else:
                        individual[nextLine[TAG]] = nextLine[ARG]
                        individual['lines'][individual['INDI'] + nextLine[TAG]] = nextFileLineNum

                nextLineNum += 1
                lineNum = nextLineNum
                if nextLineNum < fileLength:
                    nextLine = validatedFile[nextLineNum][0]
                    nextFileLineNum = validatedFile[nextLineNum][1]
            if lineNum < fileLength:
                line = validatedFile[lineNum][0]
                fileLineNum = validatedFile[nextLineNum][1]
        elif line[TAG] == 'FAM':
            family['FAM'] = line[ARG]
            family['lines'][family['FAM'] + line[TAG]] = fileLineNum
            nextLineNum = lineNum + 1
            nextLine = validatedFile[nextLineNum][0]
            nextFileLineNum = validatedFile[nextLineNum][1]
            while nextLineNum < fileLength and nextLine[TAG] != 'INDI' and nextLine[TAG] != 'FAM':
                if nextLine[TAG] == 'MARR' or nextLine[TAG] == 'DIV':
                    nextLineNum += 1
                    nextFileLineNum = validatedFile[nextLineNum][1]
                    family[nextLine[TAG]] = validatedFile[nextLineNum][0][ARG]
                    family['lines'][family['FAM'] + nextLine[TAG]] = nextFileLineNum
                elif nextLine[TAG] != 'NOTE' and nextLine[TAG] != 'HEAD' and nextLine[TAG] != 'TRLR':
                    if nextLine[TAG] == 'CHIL':
                        family['CHIL'].append(nextLine[ARG])
                        family['lines'][nextLine[ARG] + nextLine[TAG]] = nextFileLineNum
                    else:
                        family[nextLine[TAG]] = nextLine[ARG]
                        family['lines'][family['FAM'] + nextLine[TAG]] = nextFileLineNum

                nextLineNum += 1

                lineNum = nextLineNum
                if nextLineNum < fileLength:
                    nextLine = validatedFile[nextLineNum][0]
                    nextFileLineNum = validatedFile[nextLineNum][1]
        else:
            lineNum += 1
        if individual['INDI']:
            if individual['FAMS'] == []:
                individual['FAMS'] = None
            if individual['FAMC'] == []:
                individual['FAMC'] = None

            individualTable.append(individual)
            individual = {'INDI': None, 'NAME': None, 'SEX': None, 'BIRT': None, 'DEAT': None, 'FAMC': [], 'FAMS': [], 'lines': {}}

        if family['FAM']:
            if family['CHIL'] == []:
                family['CHIL'] = None

            familyTable.append(family)
            family = {'FAM': None, 'MARR': None, 'DIV': None, 'HUSB': None, 'WIFE': None, 'CHIL': [], 'lines': {}}
    return [individualTable, familyTable]

def buildIndividualCollection(gedcomCollection):
    individualTable = gedcomCollection[0]
    individualCol = []

    for individual in individualTable:
        newIndividual = {'ID': None, 'Name': None, 'Gender': None, 'Birthday': None, 'Age': None, 'Alive': None, 'Death': None, 'Child': None, 'Spouse': None, 'lines': None}
        
        newIndividual['lines'] = individual['lines']
        newIndividual['ID'] = individual['INDI']
        newIndividual['Name'] = individual['NAME']
        newIndividual['Gender'] = individual['SEX']
        newIndividual['Child'] = individual['FAMC']
        newIndividual['Spouse'] = individual['FAMS']
        
        try:
            birthday = datetime.datetime.strptime(individual['BIRT'], '%d %b %Y')
        except:
            birthday = None
        try:
            newIndividual['Birthday'] = birthday.strftime('%Y-%m-%d')
        except:
            newIndividual['Birthday'] = None
        
        date = datetime.date.today()

        if individual['DEAT'] == None:
            newIndividual['Alive'] = True
        else:
            newIndividual['Alive'] = False
            date = datetime.datetime.strptime(individual['DEAT'], '%d %b %Y')
            newIndividual['Death'] = date.strftime('%Y-%m-%d')
        
        try:
            newIndividual['Age'] = date.year - birthday.year - ((date.month, date.day) < (birthday.month, birthday.day))
        except:
            newIndividual['Age'] = None
        
        individualCol.append(newIndividual)

    return individualCol

def buildFamilyCollection(gedcomCollection):
    individualCol = gedcomCollection[0]
    familyTable = gedcomCollection[1]
    familyCol = []

    for family in familyTable:
        newFamily = {'ID': None, 'Married': None, 'Divorced': None, 'Husband ID': None, 'Husband Name': None, 'Wife ID': None, 'Wife Name': None, 'Children': None, 'lines': None}
        newFamily['lines'] = family['lines']
        newFamily['ID'] = family['FAM']
        if family['MARR']:
            newFamily['Married'] = datetime.datetime.strptime(family['MARR'], '%d %b %Y').strftime('%Y-%m-%d')
        
        if family['DIV']:
            newFamily['Divorced'] = datetime.datetime.strptime(family['DIV'], '%d %b %Y').strftime('%Y-%m-%d')

        newFamily['Husband ID'] = family['HUSB']
        newFamily['Wife ID'] = family['WIFE']
        newFamily['Children'] = family['CHIL']

        for individual in individualCol:
            if individual['INDI'] == family['HUSB']:
                newFamily['Husband Name'] = individual['NAME']
            if individual['INDI'] == family['WIFE']:
                newFamily['Wife Name'] = individual['NAME']
        
        familyCol.append(newFamily)
    
    return familyCol

def makePrettyTable(individualCol, familyCol):
    prettyIndividualTable = PrettyTable(['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse'])
    prettyFamilyTable = PrettyTable(['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children'])

    for i in individualCol:
        prettyIndividualTable.add_row([i['ID'], i['Name'], i['Gender'], i['Birthday'], i['Age'], i['Alive'], i['Death'], i['Child'], i['Spouse']])

    for f in familyCol:
        prettyFamilyTable.add_row([f['ID'], f['Married'], f['Divorced'], f['Husband ID'], f['Husband Name'], f['Wife ID'], f['Wife Name'], f['Children']])

    return [prettyIndividualTable, prettyFamilyTable]

def startApp(prettyGedcomTable):
    prettyIndividualTable = prettyGedcomTable[0]
    prettyFamilyTable = prettyGedcomTable[1]

    command = input('\nWhat would you like to do? Type \"help\" for a list of commands\n')
    print('\n')

    while command != 'exit':
        if command == 'help':
            print('----------------------Commands----------------------')
            print('individuals: print the table of individuals from the GEDCOM file.')
            print('families: print the table of families from the GEDCOM file.')
            print('exit: exit the program')
            print('help: print this help message\n')
            command = input('What would you like to do?\n')
            print('\n')
        elif command == 'individuals':
            print('----------------------Individuals----------------------')
            print(prettyIndividualTable)
            command = input('What would you like to do?\n')
            print('\n')
        elif command == 'families':
            print('----------------------Families----------------------')
            print(prettyFamilyTable)
            command = input('What would you like to do?\n')
            print('\n')
        elif command == 'exit':
            print('\n')
        else:
            print('Command \"%s\" not found. Type \"help\" for a list of commands.' % command)
            command = input('What would you like to do?\n')

    print('Goodbye!\n')

def individualError(us, ID, msg, lineNum):
    print('%s:ERROR: INDIVIDUAL: %s: %s: %s' % (lineNum, us, ID, msg))

def familyError(us, ID, msg, lineNum):
    print('%s:ERROR: FAMILY: %s: %s: %s' % (lineNum, us, ID, msg))

def individualInfo(us, ID, msg, lineNum):
    print('%s:INFO: INDIVIDUAL: %s: %s: %s' % (lineNum, us, ID, msg))

def familyInfo(us, ID, msg, lineNum):
    print('%s:INFO: FAMILY: %s: %s: %s' % (lineNum, us, ID, msg))
