import unittest
import gedcom
import us18

gedcomFile = open('../gedcom_files/us18.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
famCol = gedcom.buildFamilyCollection(collections)
indCol = gedcom.buildIndividualCollection(collections)

class testBirthMarr(unittest.TestCase):
    def testWrongFams(self):
        wrongFams = [['us18_fid1']]
        self.assertEqual(us18.noSiblingsMarried(famCol,indCol), wrongFams)

if __name__ == '__main__':
    unittest.main()
