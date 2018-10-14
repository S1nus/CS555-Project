import unittest
import gedcom
import us05

gedcomFile = open('../gedcom_files/us05.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)
famCol = gedcom.buildFamilyCollection(collections)

class TestDb4M(unittest.TestCase):
    def test_onedeadperson(self):
        self.assertEqual(len(us05.getDb4M(indiCol, famCol)), 1)

if __name__ == '__main__':
    unittest.main()
