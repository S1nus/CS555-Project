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
            if (indi['ID'] == husbID or indi['ID'] == wifeID):
                if (not indi['Death'] == None):
                    if (getDate('Death', indi) < marriageDate):
                        results.append(indi['ID'])
                        gedcom.individualError('US05', indi['ID'], 'Individual died before marriage to spouse')
    return results
