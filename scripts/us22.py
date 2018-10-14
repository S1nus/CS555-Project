import gedcom

def getIDs(collection):
    ids = []
    for c in collection:
        ids.append(c['ID'])

    return ids

def getNonUniqueIds(collection, colType):
    ids = getIDs(collection)
    nonUniqueIds = []

    for i in ids:
        if i and i not in nonUniqueIds and ids.count(i) != 1:
            nonUniqueIds.append(i)
            msg = 'ID not unique, more than one occurence found.'
            if colType == 'individual':
                gedcom.individualError('US22', i, msg)
            elif colType == 'family':
                gedcom.familyError('US22', i, msg)

    return nonUniqueIds
