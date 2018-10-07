import unittest
import gedcom
import us08

gedcomFile = open('../gedcom_files/us08.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)
famCol = gedcom.buildFamilyCollection(collections)

class TestDatesBeforeAndAfterMarriage(unittest.TestCase):
    def test_birthsBeforeAndAfterMarriage(self):
        invalidBirths = ['us08_iid3', 'us08_iid4']
        self.assertEqual(us08.birthsBeforeAndAfterMarriage(indiCol, famCol), invalidBirths)

if __name__ == '__main__':
    unittest.main()
