from datetime import datetime
import gedcom

def getDate(tag, entry):
    if entry[tag] != None:
        return datetime.strptime(entry[tag], '%Y-%m-%d')
    else:
        return None

def marriedBeforeDivorced(familyCollection):
    wrongFamList = []
    
    for family in familyCollection:
        if getDate('Married', family) == None and getDate('Divorced', family) != None:
            wrongFamList.append(family['ID'])
            gedcom.familyError('US04', family['ID'], ('Divorced %s without ever being married' % family['Divorced']))
        elif getDate('Married', family) != None and getDate('Divorced', family) != None and getDate('Married', family ) > getDate('Divorced', family):
            wrongFamList.append(family['ID'])
            gedcom.familyError('US04', family['ID'], ('Divorced %s before marriage %s' % (family['Divorced'], family['Married'])))

    return wrongFamList
