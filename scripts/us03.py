import gedcom
from datetime import datetime

def getDate(tag, entry):
    return datetime.strptime(entry[tag], '%Y-%m-%d')

def getdb4b(collection):
    db4b = []
    for person in collection:
        if not person['Death'] == None:
            if  getDate('Death', person) < getDate('Birthday', person):
                db4b.append(person['ID'])

    if not len(db4b) == 0:
        gedcom.individualError('US03', person['ID'], "This person's death is before their birth...")
    return db4b
