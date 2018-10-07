import unittest
import gedcom
import us02

gedcomFile = open('../gedcom_files/us02.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
famCol = gedcom.buildFamilyCollection(collections)
indCol = gedcom.buildIndividualCollection(collections)

class testBirthMarr(unittest.TestCase):
    def testWrongFams(self):
        wrongFams = ['us02_fid1', 'us02_fid2']
        self.assertEqual(set(us02.birthBeforeMarriage(famCol,indCol)), set(wrongFams))

if __name__ == '__main__':
    unittest.main()
