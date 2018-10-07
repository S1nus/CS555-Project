import unittest
import gedcom
import us29

gedcomFile = open('../gedcom_files/us29.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)
famCol = gedcom.buildFamilyCollection(collections)

class TestDeadPeople(unittest.TestCase):
    def test_onedeadperson(self):
        self.assertEqual(len(us29.getDead(indiCol)), 1)

if __name__ == '__main__':
    unittest.main()
