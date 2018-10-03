import gedcom
import unittest
import us09

gedcomFile = open('../gedcom_files/us09.ged', 'r')
collection = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collection)
famCol = gedcom.buildFamilyCollection(collection)

class TestAge(unittest.TestCase):
    def test_db4b(self):
        result = us09.getdb4b(indiCol)
        self.assertEqual(result, ['us09_iid4'])

if __name__ == '__main__':
    unittest.main()
