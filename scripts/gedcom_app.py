import gedcom

gedcomFile = gedcom.readFile()
validatedFile = gedcom.validateFile(gedcomFile)

gedcomCollection = gedcom.parseFile(validatedFile)
individualCollection = gedcom.buildIndividualCollection(gedcomCollection)
familyCollection = gedcom.buildFamilyCollection(gedcomCollection)

prettyGedcomTable = gedcom.makePrettyTable(individualCollection, familyCollection)

gedcom.startApp(prettyGedcomTable)
