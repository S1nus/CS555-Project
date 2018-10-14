# USER STORY UNITTEST TEMPLATE
import unittest
import gedcom
import us31

gedcomFile = open('../gedcom_files/us31.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)

class TestAllLivingSingle(unittest.TestCase):
    def test_getAllLivingSingle(self):
        livingSingle = ['us31_iid3', 'us31_iid4']
        self.assertEqual(us31.getAllLivingSingle(indiCol), livingSingle)

if __name__ == '__main__':
    unittest.main()
