from datetime import datetime
import gedcom
def getDate(tag, entry):
    if entry[tag] != None:
        return datetime.strptime(entry[tag], '%Y-%m-%d')
    else:
        return None
def birthBeforeMarriage (familyCollection, individualCollection):
	WrongFamList = []
	for family in familyCollection:
		for spouse in individualCollection:
			if family['Husband ID'] == spouse['ID'] or family['Wife ID'] == spouse['ID']:
					if getDate('Married', family) and getDate('Birthday', spouse) and getDate('Married', family) < getDate('Birthday', spouse):
						WrongFamList.append(family['ID'])
						gedcom.familyError('US02', family['ID'], ('Birthday %s after being married' % spouse['Birthday']))
	return set(WrongFamList)

