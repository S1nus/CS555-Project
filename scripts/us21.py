import gedcom

def getHusbandGender(individualCollection, familyCollection):
    reversedGenders = []
    
    for f in familyCollection:
        husbandID = f['Husband ID']
        
        for i in individualCollection:
            if i['ID'] == husbandID:
                if i['Gender'] != 'M':
                    reversedGenders.append(husbandID)
                    gedcom.familyError('US21', f['ID'], ('Husband (%s) gender should be M' % husbandID))

    return reversedGenders

def getWifeGender(individualCollection, familyCollection):
    reversedGenders = []
    
    for f in familyCollection:
        wifeID = f['Wife ID']
        
        for i in individualCollection:
            if i['ID'] == wifeID:
                if i['Gender'] != 'F':
                    reversedGenders.append(wifeID)
                    gedcom.familyError('US21', f['ID'], ('Wife (%s) should be F' % husbandID))

    return reversedGenders
