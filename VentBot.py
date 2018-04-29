# Driver Program

import Database as db
import DataNormalizer as dn

DATA = "./data/Jack_Test1.xml"

normalizedData = dn.parseXML(DATA)
db.create(normalizedData)