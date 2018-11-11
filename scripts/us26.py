import gedcom

def getInconsistencies(individualCollection, familyCollection):
    CHILDOF = 0
    CHILDREN = 0
    SPOUSE = 1
    GENDER = 2
    HUSB = 1
    WIFE = 2

    indis = {}
    fams = {}
    
    inconChildOf = []
    inconChildren = []
    inconSpouse = []
    inconHusband = []
    inconWife = []


    for indi in individualCollection:
        iid = indi['ID']
        gender = indi['Gender']
        childOf = indi['Child']
        spouseOf = indi['Spouse']
        
        try:
            indis[iid]
        except KeyError:
            indis[iid] = (childOf, spouseOf, gender)
            
    
    for fam in familyCollection:
        fid = fam['ID']
        children = fam['Children']
        husband = fam['Husband ID']
        wife = fam['Wife ID']
        
        try:
            fams[fid]
        except KeyError:
            fams[fid] = (children, husband, wife)

    for iid, iinfo in indis.items():
        childOf = iinfo[CHILDOF]
        spouseOf = iinfo[SPOUSE]
        gender = iinfo[GENDER]
        
        if childOf != None:
            for fid in childOf:
                try:
                    fam = fams[fid]
                    children = fam[CHILDREN]
                    
                    if children == None or iid not in children:
                        inconChildOf.append((iid, fid))
                        gedcom.individualError('US26', iid, ('Individual is child of %s, but the family has no entry for individual' % fid))
                except KeyError:
                    inconChildOf.append((iid, fid))
                    gedcom.individualError('US26', iid, ('Individual is child to family %s which doesn\'t exist' % fid))
        
        if spouseOf != None:
            for fid in spouseOf:
                try:
                    fam = fams[fid]
                    husband = fam[HUSB]
                    wife = fam[WIFE]
                    if gender == 'M':
                        if husband == None or iid != husband:
                            inconSpouse.append((iid, fid))
                            gedcom.individualError('US26', iid, ('Individual is husband of %s, but the family has no entry for individual' % fid))
                    elif gender == 'F':
                        if wife == None or iid != wife:
                            inconSpouse.append((iid, fid))
                            gedcom.individualError('US26', iid, ('Individual is wife of %s, but the family has no entry for individual' % fid))
                except KeyError:
                    inconSpouse.append((iid, fid))
                    gedcom.individualError('US26', iid, ('Individual is spouse in family %s which doesn\'t exist' % fid))

    for fid, finfo in fams.items():
        children = finfo[CHILDREN]
        husband = finfo[HUSB]
        wife = finfo[WIFE]

        if children != None:
            for iid in children:
                try:
                    indi = indis[iid]
                    childOf = indi[CHILDOF]
                    if childOf == None or fid not in childOf:
                        inconChildren.append((fid, iid))
                        gedcom.familyError('US26', fid, ('Family has child %s listed, but individual has no entry for family' % iid))
                except KeyError:
                    inconChildren.append((fid, iid))
                    gedcom.familyError('US26', fid, ('Family has child %s that doesn\'t exist' % iid))

        if husband != None:
            try:
                indi = indis[husband]
                spouses = indi[SPOUSE]
                if spouses != None:
                    for spouse in spouses:
                        if spouse == None or spouse != fid:
                            inconHusband.append((fid, husband))
                            gedcom.familyError('US26', fid, ('Family has husband %s listed, but individual has no entry for family' % husband))
                else:
                    inconHusband.append((fid, husband))
                    gedcom.familyError('US26', fid, ('Family has husband %s listed, but individual has no entry for family' % husband))

            except KeyError:
                inconHusband.append((fid, husband))
                gedcom.familyError('US26', fid, ('Family has husband %s that doesn\'t exist' % husband))

        if wife != None:
            try:
                indi = indis[wife]
                spouses = indi[SPOUSE]
                if spouses != None:
                    for spouse in spouses:
                        if spouse == None or spouse != fid:
                            inconWife.append((fid, wife))
                            gedcom.familyError('US26', fid, ('Family has wife %s listed, but individual has no entry for family' % wife))
                else:
                    inconWife.append((fid, wife))
                    gedcom.familyError('US26', fid, ('Family has husband %s listed, but individual has no entry for family' % wife))
            except KeyError:
                inconWife.append((fid, wife))
                gedcom.familyError('US26', fid, ('Family has wife %s that doesn\'t exist' % wife))

    return inconChildOf, inconSpouse, inconChildren, inconHusband, inconWife
