import unittest
from datetime import datetime
import gedcom

def getDate (tag, entry):
	return datetime.strptime(entry[tag],"%Y-%m-%d")

def MarriedbeforeDivorced (familyCollection):
	WrongFamList= []
	for family in familyCollection:
		if getDate("Married", family) == None or getDate("Divorced", family) == None:
			WrongFamList.append(family["ID"])
		elif getDate("Married", family ) > getDate("Divorced", family):
			WrongFamList.append(family["ID"])	
	return WrongFamList


