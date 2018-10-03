import unittest
import gedcom
import us07

gedcomFile = open('../gedcom_files/us07.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)

def allAgesUnder150(col):
    under150 = []
    for i in col:
        if i['Age'] < 150:
            retur
    
    return under150

class TestAge(unittest.TestCase):
    def test_agesOver150(self):
        agesOver150 = ['us07_iid1']
        self.assertEqual(us07.getAgesOver150(indiCol), agesOver150)

    def test_agesAreEqual(self):
        age = 218
        self.assertEqual(indi['Age'], age)

if __name__ == '__main__':
    unittest.main()
