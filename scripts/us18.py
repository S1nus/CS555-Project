import gedcom
def noSiblingsMarried(familyCollection,individualCollection):
    Husband = None
    Wife = None
    WrongFamList = []
    for family in familyCollection:
        for individual in individualCollection:
            if individual["ID"] == family["Husband ID"]:
                Husband = individual
            elif individual["ID"] == family["Wife ID"]:
                Wife = individual
        if Husband != None and Wife != None and Husband["Child"] == Wife["Child"]:
            if (Husband["Child"] != None and Wife["Child"] != None):
                WrongFamList.append(Husband["Child"])
                gedcom.familyError('US18', family['ID'], ('Husband and Wife are siblings in family: %s' % Husband['Child']), family['lines'][family['ID'] + 'FAM'])
    return WrongFamList
