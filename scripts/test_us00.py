# USER STORY UNITTEST TEMPLATE
import unittest
import gedcom
# import us00

gedcomFile = open('../gedcom_files/us00.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)
famCol = gedcom.buildFamilyCollection(collections)

class TestSomething(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
