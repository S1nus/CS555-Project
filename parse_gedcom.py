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
                    print('Invalid: %s' % line)
            except ValueError:
                print('Invalid: %s' % line)
        
    
    return validatedFile

validatedFile = validateFile(gedcomFile)
