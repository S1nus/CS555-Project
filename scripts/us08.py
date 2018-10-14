import gedcom
from datetime import datetime

def getDate(tag, entry):
    if entry[tag] != None:
        return datetime.strptime(entry[tag], '%Y-%m-%d')
    else:
        return None

def birthsBeforeAndAfterMarriage(individualCollection, familyCollection):
    invalidBirths = []
    for family in familyCollection:
        if family['Children']:
            for child in family['Children']:
                for individual in individualCollection:
                    if individual['ID'] == child:
                        birthday = getDate('Birthday', individual)
                        marriage = getDate('Married', family)
                        divorce = getDate('Divorced', family)
                        if not marriage or birthday < marriage:
                            invalidBirths.append(child)
                            gedcom.individualError('US08', child, 'Born before parents married')
                        elif marriage and divorce and birthday > divorce:
                            delta = birthday - divorce
                            if delta.days > 270:
                                invalidBirths.append(child)
                                gedcom.individualError('US08', child, 'Born more than 9 months after parents divorce')

    return invalidBirths
