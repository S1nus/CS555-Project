import gedcom

def getIDs(collection, colType):
    ids = []
    for c in collection:
        if colType == 'individual':
            ids.append((c['ID'], c['lines'][c['ID'] + 'INDI']))
        elif colType == 'family':
            ids.append((c['ID'], c['lines'][c['ID'] + 'FAM']))

    return ids

def getNonUniqueIds(collection, colType):
    idPair = getIDs(collection, colType)
    nonUniqueIds = []
    ids = []
    for i in idPair:
        ids.append(i[0])
        if i[0] and i[0] not in nonUniqueIds and ids.count(i[0]) != 1:
            nonUniqueIds.append(i[0])
            msg = 'ID not unique, more than one occurence found.'
            if colType == 'individual':
                gedcom.individualError('US22', i[0], msg, i[1])
            elif colType == 'family':
                gedcom.familyError('US22', i[0], msg, i[1])

    return nonUniqueIds
