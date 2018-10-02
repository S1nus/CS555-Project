import unittest
from datetime import datetime
import gedcom

def getDate(tag, entry):
    return datetime.strptime(entry[tag], '%Y-%m-%d')

def allDatesBeforeCurrent(collection, colType):
    today = datetime.now()

    if colType == 'individuals':
        for entry in collection:
            if entry['Birthday']:
                if getDate('Birthday', entry) > today:
                    return False
            if entry['Death']:
                if getDate('Death', entry) > today:
                    return False
        return True
    elif colType == 'families':
        for entry in collection:
            if entry['Married']:
                if getDate('Married', entry) > today:
                    return False
            if entry['Divorced']:
                if getDate('Divorced', entry) > today:
                    return False
        return True
    else:
        return False

gedcomFile = open('../gedcom_files/us01.ged', 'r')
collection = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collection)
famCol = gedcom.buildFamilyCollection(collection)

class TestAllDatesBeforeCurrent(unittest.TestCase):
    def test_individualAllDatesBeforeCurrent(self):
        self.assertTrue(allDatesBeforeCurrent(indiCol, 'individuals'))

    def test_familyAllDatesBeforeCurrent(self):
        self.assertTrue(allDatesBeforeCurrent(famCol, 'families'))

if __name__ == '__main__':
    unittest.main()
