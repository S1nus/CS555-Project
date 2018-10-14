import gedcom

def getAllLivingSingle(individualCollection):
    livingSingle = []

    for individual in individualCollection:
        iid = individual['ID']
        isAlive = individual['Alive']
        isSingle = (individual['Spouse'] == None)
        isOver30 = (individual['Age'] > 30)
        
        if isAlive and isSingle and isOver30:
            livingSingle.append(iid)
            gedcom.individualInfo('US31', iid, 'Individual is over 30 and has never married')
    
    return livingSingle
