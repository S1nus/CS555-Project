import gedcom

def getParentsParents(id, familyCollections, individualCollection):
    for family in familyCollections:
        try:
            if (id in family['Children']):
                parents = []
                parents.append(family['Husband ID'])
                parents.append(family['Wife ID'])
                break;
        except:
            parents = []
    parentsparents = []
    for parentId in parents:
        for family in familyCollections:
            try:
                if (parentId in family['Children']):
                    parentsparents.append(family['Husband ID'])
                    parentsparents.append(family['Wife ID'])
            except:
                pass;
    return parentsparents
    
def anyCousinsMarried(familyCollections, individualCollection):
    ret = []
    for i in familyCollections:
        if (bool(set(getParentsParents(i['Husband ID'], familyCollections, individualCollection)) & set(getParentsParents(i['Wife ID'], familyCollections, individualCollection)))):
            ret.append(i['ID'])
            gedcom.familyError('US19', i['ID'], 'First cousins should not be married')
    return ret
#def getCousins(familyCollections, individualCollection):
#    for fam in familyCollections:
#        print(fam)
#    for indi in individualCollection:
#        print(indi)
#
#def noCousinsMarried(familyCollection,individualCollection):
#	Husband = []
#	Wife = []
#	WrongFamList = []
#	for family in familyCollection:
#		for individual in individualCollection:
#			if individual["ID"] ==family["Husband ID"]:
#				Husband = individual
#			elif individual["ID"] == family["Wife ID"]:
#				Wife = individual
#		if Husband["Child"] == Wife["Child"]:
#			if (Husband["Child"] != None and Wife["Child"] != None):
#				WrongFamList.append(Husband["Child"])
#				gedcom.familyError('US18', family['ID'], ('Husband and Wife are siblings in family: %s' % Husband['Child']))
#	return WrongFamList
#
#
