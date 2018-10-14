# USER STORY UNITTEST TEMPLATE
import unittest
import gedcom
import us11

gedcomFile = open('../gedcom_files/us11.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)
famCol = gedcom.buildFamilyCollection(collections)
bigamousIndividuals = us11.getBigamousIndividuals(indiCol, famCol)

class TestBigamousIndividuals(unittest.TestCase):
    def test_getRightAmountofBigamies(self):
        self.assertEqual(len(bigamousIndividuals), 4)
    
    def test_getAllBigamies(self):
        bigamies = [('us11_iid1', 'us11_iid2', 'us11_iid5'), ('us11_iid1', 'us11_iid2', 'us11_iid6'), ('us11_iid1', 'us11_iid5', 'us11_iid6'), ('us11_iid6', 'us11_iid1', 'us11_iid7')]
        self.assertEqual(bigamies, bigamousIndividuals)

if __name__ == '__main__':
    unittest.main()
