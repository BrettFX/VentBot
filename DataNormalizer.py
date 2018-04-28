import pandas as pd

# Format of normalizedData: [{phoneKey : phoneValue, typeKey : typeValue, subjectKey, subjectValue, bodyKey, bodyValue}, ... ]
PHONE_KEY = "phoneKey"
TYPE_KEY = "typeKey"
SUBJECT_KEY = "subjectKey"
BODY_KEY = "bodyKey"

def parseCSV(csvPath):
    return

def parseXML(xmlPath):
    xmlFile = open(xmlPath, "r")
    lines = xmlFile.readlines()
    xmlFile.close()
    
    print(lines)
    return
    

def run():
    return

# Run the program
run()