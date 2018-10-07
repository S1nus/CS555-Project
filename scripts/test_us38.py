import unittest
import gedcom
import us38

gedcomFile = open('../gedcom_files/us38.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)
famCol = gedcom.buildFamilyCollection(collections)

class TestDeadPeople(unittest.TestCase):
    def test_onedeadperson(self):
        self.assertEqual(len(us38.upcomingBdays(indiCol)), 1)

if __name__ == '__main__':
    unittest.main()
