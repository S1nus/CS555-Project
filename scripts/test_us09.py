# USER STORY UNITTEST TEMPLATE
import unittest
import gedcom
import us09

gedcomFile = open('../gedcom_files/us09.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)
famCol = gedcom.buildFamilyCollection(collections)

class TestBirthBeforeDeathOfParents(unittest.TestCase):
    def test_birthBeforeDeathOfParents(self):
        birthsAfterDeaths = us09.getBirthsAfterDeathsOfParents(indiCol, famCol)
        actualBirthsAfterDeaths = ['us09_iid3', 'us09_iid6']
        self.assertEqual(birthsAfterDeaths, actualBirthsAfterDeaths)

if __name__ == '__main__':
    unittest.main()
