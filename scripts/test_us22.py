import unittest
import gedcom

def getIDs(collection):
    ids = []
    for c in collection:
        ids.append(c['ID'])

    return ids

def idExists(ids):
    for i in ids:
        if i == None:
            return False
    
    return True

def idUnique(ids):
    if len(ids) == len(set(ids)):
        return True
    else:
        return False

gedcomFile = open('../gedcom_files/us22.ged', 'r')
collections = gedcom.parseFile(gedcom.validateFile(gedcomFile))
indiCol = gedcom.buildIndividualCollection(collections)
famCol = gedcom.buildFamilyCollection(collections)
indiIDs = getIDs(indiCol)
famIDs = getIDs(famCol)

class TestUniqueIds(unittest.TestCase):
    def test_indiExists(self):
        self.assertTrue(idExists(indiIDs))

    def test_famExists(self):
        self.assertTrue(idExists(famIDs))

    def test_indiUnique(self):
        self.assertTrue(idUnique(indiIDs))

    def test_famUnique(self):
        self.assertTrue(idUnique(famIDs))

if __name__ == '__main__':
    unittest.main()
