import xml.etree.ElementTree as et
import re

# Format of normalizedData: [{phoneKey : phoneValue, typeKey : typeValue, subjectKey, subjectValue, bodyKey, bodyValue}, ... ]
PHONE_KEY = "address"
TYPE_KEY = "type"
SUBJECT_KEY = "subject"
BODY_KEY = "body"

TARGET_COLS = "address, type, subject, body"

def parseCSV(csvPath):
    return None

def parseXML(xmlPath):
	# A list of dictionaries
	normalizedData = []

	xmlData = et.parse(xmlPath).getroot()
	elements = xmlData.findall("sms")
    
	for attributes in elements:
		dataRow = {}
		for key in attributes.keys():
    		# Only insert target columns
			if key in TARGET_COLS:        
				value = attributes.get(key)

				# Replace all quotes and apostrophes with apostrophes 
				value = re.sub("[\'\"]", "\'", value)    
				dataRow[key] = value
	    
		normalizedData.append(dataRow)

	return normalizedData