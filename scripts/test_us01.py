import unittest
import gedcom

def dateBeforeCurrent(collection, colType):
    dateList = []
    dateFormat = '%Y-%m-%d'
    if colType == 'individuals':
        for c in collection:
            if c['Birthday']:
                try:
                    datetime.datetime.strptime(c['Birthday'], dateFormat)
                except ValueError:
                    dateList.append(c['ID'], 
            dateList.append(c['Birthday'], c['Death'], c[], c[]
    elif colType == 'families':
    else:
        return False

gedcomFile = open('../gedcom_files/us01.ged', 'r')
tables = ged.parseFile(ged.validateFile(gedcomFile))
indiCol = ged.buildIndividualCollection(tables[0])
famCol = ged.buildFamilyCollection(tables[1], indiCol)
indiIDs = getIDs(indiCol)
famIDs = getIDs(famCol)

class datesBeforeCurrent(unittest.TestCase):
    def test_individualAllDatesBeforeCurrent(self):
        self.assertTrue(allDatesBeforeCurrent(indiCol, 'individuals'))

    def test_familyAllDatesBeforeCurrent(self):
        self.assertTrue(allDatesBeforeCurrent(famCol, 'families'))

if __name__ == '__main__':
    unittest.main()
