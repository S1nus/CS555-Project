import gedcom
import us01
import us02
import us03
import us04
import us05
import us06
import us07
import us08
import us11
import us18
import us21
import us22
import us29
import us31
import us38

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
us03.getdb4b(individualCollection)
us04.marriedBeforeDivorced(familyCollection)
us05.getDb4M(individualCollection, familyCollection)
us06.getDivb4D(individualCollection, familyCollection)
us07.getAgesOver150(individualCollection)
us08.birthsBeforeAndAfterMarriage(individualCollection, familyCollection)
us11.getBigamousIndividuals(individualCollection, familyCollection)
us18.noSiblingsMarried(familyCollection, individualCollection)
us21.getHusbandGender(individualCollection, familyCollection)
us21.getWifeGender(individualCollection, familyCollection)
us22.getNonUniqueIds(individualCollection, 'individual')
us22.getNonUniqueIds(familyCollection, 'family')
us29.getDead(individualCollection)
us31.getAllLivingSingle(individualCollection)
us38.upcomingBdays(individualCollection)

try:
    gedcom.startApp(prettyGedcomTable)
except KeyboardInterrupt:
    print('\nGoodbye!\n')


