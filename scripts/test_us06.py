import unittest
import gedcom
import us06

gedcomFile = open('../gedcom_files/us06.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)
famCol = gedcom.buildFamilyCollection(collections)

class TestDivb4D(unittest.TestCase):
    def test_onedeadperson(self):
        self.assertEqual(len(us06.getDivb4D(indiCol, famCol)), 1)

if __name__ == '__main__':
    unittest.main()
