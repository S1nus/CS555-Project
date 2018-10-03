import unittest
import gedcom
import us22

gedcomFile = open('../gedcom_files/us22.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)
famCol = gedcom.buildFamilyCollection(collections)

class TestUniqueIds(unittest.TestCase):
    def test_nonUniqueIndividuals(self):
        nonUniqueIds = ['us22_iid2']
        self.assertEqual(us22.getNonUniqueIds(indiCol, 'individual'), nonUniqueIds)

    def test_nonUniqueFamilies(self):
        nonUniqueIds = ['us22_fid1']
        self.assertEqual(us22.getNonUniqueIds(famCol, 'family'), nonUniqueIds)

if __name__ == '__main__':
    unittest.main()
