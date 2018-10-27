import datetime
import gedcom

def getDate(tag, entry):
    if entry[tag] != None:
        return datetime.datetime.strptime(entry[tag], '%Y-%m-%d')
    else:
        return None

def getBirthsAfterDeathsOfParents(individualCollection, familyCollection):
    birthsAfterDeaths = []
    for family in familyCollection:
        parentIDs = { 'mom': family['Wife ID'], 'dad': family['Husband ID'] }
        childrenIDs = family['Children']
        momDeath = None
        dadDeath = None
        childBirths = []
        if childrenIDs:
            for individual in individualCollection:
                if individual['ID'] == parentIDs['mom']:
                    momDeath = getDate('Death', individual)

                if individual['ID'] == parentIDs['dad']:
                    dadDeath = getDate('Death', individual)

                if individual['ID'] in childrenIDs:
                    childBirths.append([individual['ID'], getDate('Birthday', individual)])
        
        for births in childBirths:
            if momDeath and births[1] and births[1] > momDeath:
                gedcom.individualError('US09', births[0], ('Child born %s after death of mother %s' % (births[1], momDeath)))
                birthsAfterDeaths.append(births[0])

            if dadDeath and births[1] and births[1] > dadDeath and (births[1] - dadDeath).days > 270:
                gedcom.individualError('US09', births[0], ('Child born %s more than 9 months after death of father %s' % (births[1], dadDeath)))
                birthsAfterDeaths.append(births[0])
    
    return birthsAfterDeaths
