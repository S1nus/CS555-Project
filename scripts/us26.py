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
        lines = indi['lines']
        
        try:
            indis[iid]
        except KeyError:
            indis[iid] = (childOf, spouseOf, gender, lines)
            
    
    for fam in familyCollection:
        fid = fam['ID']
        children = fam['Children']
        husband = fam['Husband ID']
        wife = fam['Wife ID']
        lines = fam['lines']
        
        try:
            fams[fid]
        except KeyError:
            fams[fid] = (children, husband, wife, lines)

    for iid, iinfo in indis.items():
        childOf = iinfo[CHILDOF]
        spouseOf = iinfo[SPOUSE]
        gender = iinfo[GENDER]
        lines = iinfo[3]
        
        if childOf != None:
            for fid in childOf:
                try:
                    fam = fams[fid]
                    children = fam[CHILDREN]
                    
                    if children == None or iid not in children:
                        inconChildOf.append((iid, fid))
                        gedcom.individualError('US26', iid, ('Individual is child of %s, but the family has no entry for individual' % fid), lines[fid + 'FAMC'])
                except KeyError:
                    inconChildOf.append((iid, fid))
                    gedcom.individualError('US26', iid, ('Individual is child to family %s which doesn\'t exist' % fid), lines[fid + 'FAMC'])
        
        if spouseOf != None:
            for fid in spouseOf:
                try:
                    fam = fams[fid]
                    husband = fam[HUSB]
                    wife = fam[WIFE]
                    if gender == 'M':
                        if husband == None or iid != husband:
                            inconSpouse.append((iid, fid))
                            gedcom.individualError('US26', iid, ('Individual is husband of %s, but the family has no entry for individual' % fid), lines[fid + 'FAMS'])
                    elif gender == 'F':
                        if wife == None or iid != wife:
                            inconSpouse.append((iid, fid))
                            gedcom.individualError('US26', iid, ('Individual is wife of %s, but the family has no entry for individual' % fid), lines[fid + 'FAMS'])
                except KeyError:
                    inconSpouse.append((iid, fid))
                    gedcom.individualError('US26', iid, ('Individual is spouse in family %s which doesn\'t exist' % fid), lines[fid + 'FAMS'])

    for fid, finfo in fams.items():
        children = finfo[CHILDREN]
        husband = finfo[HUSB]
        wife = finfo[WIFE]
        lines = finfo[3]

        if children != None:
            for iid in children:
                try:
                    indi = indis[iid]
                    childOf = indi[CHILDOF]
                    if childOf == None or fid not in childOf:
                        inconChildren.append((fid, iid))
                        gedcom.familyError('US26', fid, ('Family has child %s listed, but individual has no entry for family' % iid), lines[iid + 'CHIL'])
                except KeyError:
                    inconChildren.append((fid, iid))
                    gedcom.familyError('US26', fid, ('Family has child %s that doesn\'t exist' % iid), lines[iid + 'CHIL'])

        if husband != None:
            try:
                indi = indis[husband]
                spouses = indi[SPOUSE]
                if spouses != None:
                    for spouse in spouses:
                        if spouse == None or spouse != fid:
                            inconHusband.append((fid, husband))
                            gedcom.familyError('US26', fid, ('Family has husband %s listed, but individual has no entry for family' % husband), lines[fid + 'HUSB'])
                else:
                    inconHusband.append((fid, husband))
                    gedcom.familyError('US26', fid, ('Family has husband %s listed, but individual has no entry for family' % husband), lines[fid + 'HUSB'])

            except KeyError:
                inconHusband.append((fid, husband))
                gedcom.familyError('US26', fid, ('Family has husband %s that doesn\'t exist' % husband), lines[fid + 'HUSB'])

        if wife != None:
            try:
                indi = indis[wife]
                spouses = indi[SPOUSE]
                if spouses != None:
                    for spouse in spouses:
                        if spouse == None or spouse != fid:
                            inconWife.append((fid, wife))
                            gedcom.familyError('US26', fid, ('Family has wife %s listed, but individual has no entry for family' % wife), lines[fid + 'WIFE'])
                else:
                    inconWife.append((fid, wife))
                    gedcom.familyError('US26', fid, ('Family has husband %s listed, but individual has no entry for family' % wife), lines[fid + 'WIFE'])
            except KeyError:
                inconWife.append((fid, wife))
                gedcom.familyError('US26', fid, ('Family has wife %s that doesn\'t exist' % wife), lines[fid + 'WIFE'])

    return inconChildOf, inconSpouse, inconChildren, inconHusband, inconWife
