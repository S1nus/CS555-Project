# USER STORY UNITTEST TEMPLATE
import unittest
import gedcom
import us26

gedcomFile = open('../gedcom_files/us26.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)
famCol = gedcom.buildFamilyCollection(collections)

class TestConsistency(unittest.TestCase):
    def test_childOf_consistent(self):
        inconChildOf = [('us26_iid1', 'us26_fid2')]
        childOf = us26.getInconsistencies(indiCol ,famCol)[0]
        self.assertEqual(childOf, inconChildOf)
    
    def test_spouse_consistent(self):
        inconSpouse = [('us26_iid2', 'us26_fid1'), ('us26_iid2', 'us26_fid2')]
        spouse = us26.getInconsistencies(indiCol ,famCol)[1]
        self.assertEqual(spouse, inconSpouse)
    
    def test_children_consistent(self):
        inconChildren = [('us26_fid1', 'us26_iid3')]
        children = us26.getInconsistencies(indiCol ,famCol)[2]
        self.assertEqual(children, inconChildren)
    
    def test_husband_consistent(self):
        inconHusband = [('us26_fid1', 'us26_iid1')]
        husband = us26.getInconsistencies(indiCol ,famCol)[3]
        self.assertEqual(husband, inconHusband)
    
    def test_wife_consistent(self):
        inconWife = []
        wife = us26.getInconsistencies(indiCol ,famCol)[4]
        self.assertEqual(wife, inconWife)

if __name__ == '__main__':
    unittest.main()
