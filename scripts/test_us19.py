import unittest
import gedcom
import us19

gedcomFile = open('../gedcom_files/us19.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
famCol = gedcom.buildFamilyCollection(collections)
indCol = gedcom.buildIndividualCollection(collections)

class testRedneckRomance(unittest.TestCase):
    def testRedneckRomance(self):
        marriedCousins = us19.anyCousinsMarried(famCol, indCol)
        self.assertEqual(len(marriedCousins), 1)

if __name__ == '__main__':
    unittest.main()
