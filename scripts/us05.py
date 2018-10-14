import gedcom
from datetime import datetime

def getDate(tag, entry):
    if entry[tag]:
        return datetime.strptime(entry[tag], '%Y-%m-%d')
    else:
        return None

def getDb4M(people, fams):
    results = []
    for fam in fams:
        husbID = fam['Husband ID']
        wifeID = fam['Wife ID']
        marriageDate = getDate('Married', fam)
        for indi in people:
            if (indi['ID'] == husbID or indi['ID'] == wifeID):
                if not indi['Alive']:
                    if (getDate('Death', indi) and getDate('Death', indi) < marriageDate):
                        results.append(indi['ID'])
                        gedcom.individualError('US05', indi['ID'], 'Individual died before marriage to spouse')
    return results
