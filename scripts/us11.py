import gedcom
import datetime
from operator import itemgetter

def getDate(tag, entry):
    if entry[tag]:
        return datetime.datetime.strptime(entry[tag], '%Y-%m-%d')
    else:
        return None

def getIndividualMarriageAndDivorceDates(iid, families, familyCollection):
    dateTuples = []

    if families and len(families) >= 2:
        for family in familyCollection:
            fid = family['ID']
            if fid in families:
                spouseID = None
                
                if iid == family['Husband ID']:
                    spouseID = family['Wife ID']
                elif iid == family['Wife ID']:
                    spouseID = family['Husband ID']

                dateTuples.append((fid, iid, spouseID, getDate('Married', family), getDate('Divorced', family), family['lines']))
        dateTuples = sorted(dateTuples, key=itemgetter(3))
    else:
        dateTuples = None

    return dateTuples

def getBigamousIndividuals(individualCollection, familyCollection):
    bigamousIndividuals = []

    for individual in individualCollection:
        iid = individual['ID']
        families = individual['Spouse']
        dateTuples = getIndividualMarriageAndDivorceDates(iid, families, familyCollection)
        
        if dateTuples:
            index = 1
            while index < len(dateTuples):
                prevDates = dateTuples[index - 1]
                prevMarriage = prevDates[3]
                prevDivorce = prevDates[4]
                
                curIndex = index

                while curIndex < len(dateTuples):
                    curDates = dateTuples[curIndex]
                    curMarriage = curDates[3]
                    curDivorce = curDates[4]
                    marriedWhileMarried = curMarriage > prevMarriage
                    marriedBeforeDivorce = (prevDivorce and curMarriage and prevDivorce > curMarriage)
                    if marriedWhileMarried or marriedBeforeDivorce:
                        bigamousIndividuals.append((iid, prevDates[2], curDates[2]))
                        msg = 'Individual is bigamous, married to %s before divorce to %s' % (curDates[2], prevDates[2])
                        gedcom.individualError('US11', iid, msg, curDates[5][curDates[0] + 'MARR'])
                    
                    curIndex = curIndex + 1

                index = index + 1

    return bigamousIndividuals
