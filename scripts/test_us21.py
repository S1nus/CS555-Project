import unittest
import gedcom
import us21

gedcomFile = open('../gedcom_files/us21.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)
famCol = gedcom.buildFamilyCollection(collections)

class TestSomething(unittest.TestCase):
    def test_HusbandReversedRoles(self):
        reversedHusbandGenders = ['us21_iid1']
        self.assertEqual(us21.getHusbandGender(indiCol, famCol), reversedHusbandGenders)

    def test_WifeReversedRoles(self):
        reversedWifeGenders = []
        self.assertEqual(us21.getWifeGender(indiCol, famCol), reversedWifeGenders)
if __name__ == '__main__':
    unittest.main()
