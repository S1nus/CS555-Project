import gedcom
from datetime import datetime

def getDate(tag, entry):
    return datetime.strptime(entry[tag], '%Y-%m-%d')

def getDb4M(people, fams):
    results = []
    for fam in fams:
        husbID = fam['Husband ID']
        wifeID = fam['Wife ID']
        marriageDate = getDate('Married', fam)
        for indi in people:
            if (not indi['Death'] == None):
                if (getDate('Death', indi) < marriageDate):
                    results.append(indi['ID'])
    return results

#def getDead(people):
#    dead = [] 
#    for person in people:
#        if (not person["Death"] == None):
#            if (getDate("Death", person) < datetime.now()):
#                dead.append(person['ID'])
#                print('NOTICE: INDIVIDUAL: US29: %s: Is deceased' % person['ID'])
#    return dead
