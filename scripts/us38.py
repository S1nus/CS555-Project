import gedcom
from datetime import datetime

def getDate(tag, entry):
    return datetime.strptime(entry[tag], '%Y-%m-%d')

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
        month = getDate('Birthday', person).month
        day = getDate('Birthday', person).day
        daysUntil = daysUntilBday(month, day)
        if daysUntil <= 30:
            results.append(person['ID'])
    return results
