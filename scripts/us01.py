import gedcom
from datetime import datetime

def getDate(tag, entry):
    return datetime.strptime(entry[tag], '%Y-%m-%d')

def getFutureDates(collection, colType):
    futureDates = []
    today = datetime.now()

    if colType == 'individuals':
        for individual in collection:
            if individual['Birthday']:
                if getDate('Birthday', individual) > today:
                    futureDates.append([individual['ID'], 'Birthday'])
                    gedcom.individualError('US01', individual['ID'], ('Birthday %s occurs in the future.' % individual['Birthday']))
            if individual['Death']:
                if getDate('Death', individual) > today:
                    futureDates.append([individual['ID'], 'Death'])
                    gedcom.individualError('US01', individual['ID'], ('Death %s occurs in the future.' % individual['Death']))
        return futureDates
    elif colType == 'families':
        for family in collection:
            if family['Married']:
                if getDate('Married', family) > today:
                    futureDates.append([family['ID'], 'Married'])
                    gedcom.familyError('US01', family['ID'], ('Marriage date %s occurs in the future.' % family['Married']))
            if family['Divorced']:
                if getDate('Divorced', family) > today:
                    futureDates.append([family['ID'], 'Divorced'])
                    gedcom.familyError('US01', family['ID'], ('Divorce date %s occurs in the future.' % family['Divorced']))
        return futureDates
    else:
        return futureDates
