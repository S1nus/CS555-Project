import unittest
import gedcom
import us01

gedcomFile = open('../gedcom_files/us01.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)
famCol = gedcom.buildFamilyCollection(collections)

class TestFutureDates(unittest.TestCase):
    def test_individualFutureDates(self):
        futureDates = [['us01_iid1', 'Death'], ['us01_iid3', 'Birthday']]
        self.assertEqual(us01.getFutureDates(indiCol, 'individuals'), futureDates)

    def test_familyFutureDates(self):
        futureDates = [['us01_fid1', 'Married']]
        self.assertEqual(us01.getFutureDates(famCol, 'families'), futureDates)

if __name__ == '__main__':
    unittest.main()
