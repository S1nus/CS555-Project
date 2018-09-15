import datetime

level0 = frozenset(('INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE'))
level1 = frozenset(('NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'))
level2 = frozenset(['DATE'])

validTags = [level0, level1, level2]
noArgumentTags = [frozenset(('HEAD', 'TRLR')), frozenset(('BIRT', 'DEAT', 'MARR', 'DIV'))]

gedcomFileName = 'family.ged'
gedcomFile = open(gedcomFileName, 'r')
validatedFile = []

def validateLine(gedcomLine):
    line = gedcomLine.strip().split(' ', 2)
    if len(line) == 0:
        return 'invalid'
    elif len(line) == 1:
        return 'invalid'
    elif len(line) == 2:
        tag = line[1]
        try:
            level = int(line[0])
        except ValueError:
            return 'invalid'

        if level >= 0 and level < len(noArgumentTags) and tag in noArgumentTags[level]:
            return [level, tag, None]
        else:
            return 'invalid'
    elif len(line) == 3:
        if line[2].strip() == 'INDI' or line[2].strip() == 'FAM':
            tag = line[2]
            arguments = line[1]
        else:
            tag = line[1]
            arguments = line[2]
            if tag == 'INDI' or tag == 'FAM':
                return 'invalid'
        try:
            level = int(line[0])
        except ValueError:
            return 'invalid'

        if level >= 0 and level < len(noArgumentTags) and tag in noArgumentTags[level]:
            return 'invalid'

        if level >= 0 and level < len(validTags) and tag in validTags[level]:
            if tag == 'DATE':
                try:
                    datetime.datetime.strptime(arguments, '%d %b %Y')
                    validity = [level, tag, arguments]
                except ValueError:
                    validity =  'invalid'
                return validity
            else:
                return [level, tag, arguments]
        else:
            return 'invalid'
    else:
        return 'invalid'

for line in gedcomFile:
    validatedLine = validateLine(line)
    if validatedLine != 'invalid':
        validatedFile.append(validatedLine)

