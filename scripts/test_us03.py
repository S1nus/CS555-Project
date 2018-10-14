import gedcom
import unittest
import us03

gedcomFile = open('../gedcom_files/us03.ged', 'r')
collection = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collection)
famCol = gedcom.buildFamilyCollection(collection)

class TestAge(unittest.TestCase):
    def test_db4b(self):
        result = us03.getdb4b(indiCol)
        self.assertEqual(result, ['us03_iid4'])

if __name__ == '__main__':
    unittest.main()
