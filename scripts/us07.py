import gedcom

def getAgesOver150(individualCollection):
    over150 = []
    
    for individual in individualCollection:
        if individual['Age'] >= 150:
            over150.append(individual['ID'])
            gedcom.individualError('US07', individual['ID'], 'More than 150 years old - Birth date %s (%s years old)' % individual['Birthday'], individual['Age'])

    return over150
