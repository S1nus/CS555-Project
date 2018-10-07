import gedcom
import us01
import us02
import us04
import us07
import us09
import us21
import us22

try:
    gedcomFile = gedcom.readFile()
except KeyboardInterrupt:
    print('\nGoodbye!\n')

validatedFile = gedcom.validateFile(gedcomFile)

gedcomCollection = gedcom.parseFile(validatedFile)
individualCollection = gedcom.buildIndividualCollection(gedcomCollection)
familyCollection = gedcom.buildFamilyCollection(gedcomCollection)

prettyGedcomTable = gedcom.makePrettyTable(individualCollection, familyCollection)

us01.getFutureDates(individualCollection)
us01.getFutureDates(familyCollection)
us02.birthBeforeMarriage(familyCollection, individualCollection)
us04.marriedBeforeDivorced(familyCollection)
us07.getAgesOver150(individualCollection)
us09.getdb4b(individualCollection)
us21.getHusbandGender(individualCollection, familyCollection)
us21.getWifeGender(individualCollection, familyCollection)
us22.getNonUniqueIds(individualCollection, 'individual')
us22.getNonUniqueIds(familyCollection, 'family')

try:
    gedcom.startApp(prettyGedcomTable)
except KeyboardInterrupt:
    print('\nGoodbye!\n')


