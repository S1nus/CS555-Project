# USER STORY UNITTEST TEMPLATE
import unittest
import gedcom
import us40

gedcomFile = open('../gedcom_files/us40.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)
famCol = gedcom.buildFamilyCollection(collections)

class TestLineNumbers(unittest.TestCase):
    def test_rightLineNumber(self):
        self.assertEqual(us40.getLineNum(indiCol[0], indiCol[0]['ID'], 'NAME'), 4)

    def test_rightLineNumberFam(self):
        self.assertEqual(us40.getLineNum(famCol[0], famCol[0]['Children'][0], 'CHIL'), 35)
    def test_noLineNumber(self):
        self.assertEqual(us40.getLineNum(indiCol[0], indiCol[0]['ID'], 'FAMC'), 0)

if __name__ == '__main__':
    unittest.main()
