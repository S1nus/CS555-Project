import gedcom
import datetime

def getDate(tag, entry):
    noDate = datetime.datetime(1, 1, 1)
    
    # Collection doesn't have given date tag
    try:
        dateString = entry[tag]
    except KeyError:
        return noDate 
    
    # Collection has given date tag, return date if it exists,
    # or extremely small date if date is missing from tag
    if dateString:
        return datetime.datetime.strptime(dateString, '%Y-%m-%d')
    else:
        return noDate

def getFutureDates(collection):
    futureDates = []
    today = datetime.datetime.now()

    for entry in collection:
        if getDate('Birthday', entry) > today:
            futureDates.append([entry['ID'], 'Birthday'])
            gedcom.individualError('US01', entry['ID'], ('Birthday %s occurs in the future.' % entry['Birthday']))
        if getDate('Death', entry) > today:
            futureDates.append([entry['ID'], 'Death'])
            gedcom.individualError('US01', entry['ID'], ('Death %s occurs in the future.' % entry['Death']))
        if getDate('Married', entry) > today:
            futureDates.append([entry['ID'], 'Married'])
            gedcom.familyError('US01', entry['ID'], ('Marriage date %s occurs in the future.' % entry['Married']))
        if getDate('Divorced', entry) > today:
            futureDates.append([entry['ID'], 'Divorced'])
            gedcom.familyError('US01', entry['ID'], ('Divorce date %s occurs in the future.' % entry['Divorced']))
    
    return futureDates
