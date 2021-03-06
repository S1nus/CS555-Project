import gedcom
from datetime import datetime

def getDate(tag, entry):
    if entry[tag]:
        return datetime.strptime(entry[tag], '%Y-%m-%d')
    else:
        return None

def daysUntilBday(month, day):
    now = datetime.now()
    delta1 = datetime(now.year, month, day) - now
    delta2 = datetime(now.year + 1, month, day) - now
    if delta1.days < 0 and delta2.days > 0:
        return delta2.days
    elif delta2.days < 0 and delta1.days > 0:
        return delta1.days
    else:
        return min(delta1.days, delta2.days)

def upcomingBdays(people):
    results = []
    for person in people:
        birthday = getDate('Birthday', person)
        if birthday != None:
            month = getDate('Birthday', person).month
            day = getDate('Birthday', person).day
            daysUntil = daysUntilBday(month, day)
            if daysUntil <= 30:
                results.append(person['ID'])
                print('%s:NOTICE: INDIVIDUAL: US38: %s: Has a birthday in %s days!' % (person['lines'][person['ID'] + 'BIRT'], person['ID'], daysUntil))
    return results
