import unittest
import parse_gedcom as ged

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

gedcomFile = open('test.ged', 'r')
tables = ged.parseFile(ged.validateFile(gedcomFile))
indiCol = ged.buildIndividualCollection(tables[0])
famCol = ged.buildFamilyCollection(tables[1], indiCol)
indiIDs = getIDs(indiCol)
famIDs = getIDs(famCol)

class uniqueIdTest(unittest.TestCase):
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
