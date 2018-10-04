import unittest
import gedcom
import us04

gedcomFile = open('../gedcom_files/us04.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
famCol = gedcom.buildFamilyCollection(collections)

class testMarrDiv(unittest.TestCase):
    def testWrongFams(self):
        wrongFams = ['us04_fid1', 'us04_fid2']
        self.assertEqual(us04.marriedBeforeDivorced(famCol), wrongFams)

if __name__ == '__main__':
    unittest.main()
