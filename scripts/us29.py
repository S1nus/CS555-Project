import gedcom
from datetime import datetime

def getDate(tag, entry):
    return datetime.strptime(entry[tag], '%Y-%m-%d')

def getDead(people):
    dead = [] 
    for person in people:
        if (not person["Death"] == None):
            if (getDate("Death", person) < datetime.now()):
                dead.append(person['ID'])
    return dead
