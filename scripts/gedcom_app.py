import gedcom

try:
    gedcomFile = gedcom.readFile()
except KeyboardInterrupt:
    print('\nGoodbye!\n')

validatedFile = gedcom.validateFile(gedcomFile)

gedcomCollection = gedcom.parseFile(validatedFile)
individualCollection = gedcom.buildIndividualCollection(gedcomCollection)
familyCollection = gedcom.buildFamilyCollection(gedcomCollection)

prettyGedcomTable = gedcom.makePrettyTable(individualCollection, familyCollection)

try:
    gedcom.startApp(prettyGedcomTable)
except KeyboardInterrupt:
    print('\nGoodbye!\n')
