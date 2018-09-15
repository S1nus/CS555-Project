level0 = frozenset(('INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE'))
level1 = frozenset(('NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'))
level2 = frozenset(['DATE'])
validTags = [level0, level1, level2]
noArgs = [frozenset(('HEAD', 'TRLR')), frozenset(('BIRT', 'DEAT', 'MARR', 'DIV'))]

gedcomFileName = 'myInput.ged'
gedcomFile = open(gedcomFileName, 'r')

def leapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return 'true'
            else:
                return 'false'
        else:
            return 'true'
    else:
        return 'false'

def validDate(date):
    validMonths = frozenset(('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'))
    thirtyDayMonths = frozenset(('APR', 'JUN', 'NOV', 'SEP'))
    
    if len(date) != 3:
        return 'N'

    try:
        day = int(date[0])
        year = int(date[2])
    except ValueError:
        return 'N'

    month = date[1]

    if month in validMonths and day >= 1 and day <= 31:
        if month == 'FEB':
            if leapYear(year) == 'true':
                if day <= 29:
                    return 'Y'
                else:
                    return 'N'
            else:
                if day <= 28:
                    return 'Y'
                else:
                    return 'N'
        elif month in thirtyDayMonths:
            if day <= 30:
                return 'Y'
            else:
                return 'N'
        else:
            return 'Y'
    else:
        return 'N'

def validateLine(gedcomLine):
    line = gedcomLine.strip().split(' ', 2)
    if len(line) == 0:
        return '%s|N' % line
    elif len(line) == 1:
        return '%s|N' % line[0]
    elif len(line) == 2:
        tag = line[1]
        try:
            level = int(line[0])
        except ValueError:
            return '%s|%s|N' % (line[0], tag)

        if level >= 0 and level < len(noArgs) and tag in noArgs[level]:
            return '%s|%s|Y' % (level, tag)
        else:
            return '%s|%s|N' % (level, tag)
    elif len(line) == 3:
        if line[2].strip() == 'INDI' or line[2].strip() == 'FAM':
            tag = line[2]
            arguments = line[1]
        else:
            tag = line[1]
            arguments = line[2]
            if tag == 'INDI' or tag == 'FAM':
                return '%s|%s|N|%s' % (line[0], tag, arguments)
        try:
            level = int(line[0])
        except ValueError:
            return '%s|%s|N|%s' % (line[0], tag, arguments)

        if level >= 0 and level < len(noArgs) and tag in noArgs[level]:
            return '%s|%s|N|%s' % (level, tag, arguments)

        if level >= 0 and level < len(validTags) and tag in validTags[level]:
            if tag == 'DATE':
                valid = validDate(arguments.split())
                return '%s|%s|%s|%s' % (level, tag, valid, arguments)
            else:
                return '%s|%s|Y|%s' % (level, tag, arguments)
        else:
            return '%s|%s|N|%s' % (level, tag, arguments)
    else:
        return '%s|N' % line

for line in gedcomFile:
    print('--> %s' % line.strip())
    print('<-- %s' % validateLine(line))

