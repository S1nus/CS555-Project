import unittest
import gedcom
import us07

gedcomFile = open('../gedcom_files/us07.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)

class TestAge(unittest.TestCase):
    def test_agesOver150(self):
        agesOver150 = ['us07_iid1']
        self.assertEqual(us07.getAgesOver150(indiCol), agesOver150)
    
    def test_agesEqual(self):
        age = 213
        self.assertEqual(indiCol[0]['Age'], age)

if __name__ == '__main__':
    unittest.main()
