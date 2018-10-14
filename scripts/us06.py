import gedcom
from datetime import datetime

def getDate(tag, entry):
    return datetime.strptime(entry[tag], '%Y-%m-%d')

def getDivb4D(people, fams):
    results = []
    for fam in fams:
        husbID = fam['Husband ID']
        wifeID = fam['Wife ID']
        if (not fam['Divorced'] == None):
            divorceDate = getDate('Divorced', fam)
            for indi in people:
                if (indi['ID'] == husbID or indi['ID'] == wifeID):
                    if (not indi['Death'] == None):
                        if (getDate('Death', indi) < divorceDate):
                            results.append(fam['ID'])
                            gedcom.familyError('US06', fam['ID'], 'Divorce occurs after death of both spouses')
    return results

#def getDead(people):
#    dead = [] 
#    for person in people:
#        if (not person["Death"] == None):
#            if (getDate("Death", person) < datetime.now()):
#                dead.append(person['ID'])
#                print('NOTICE: INDIVIDUAL: US29: %s: Is deceased' % person['ID'])
#    return dead
