import Database as db
import DataNormalizer as dn
import sqlite3
import pandas as pd

DATA = "./data/Jack_Test1.xml"

normalizedData = dn.parseXML(DATA)
db.create(normalizedData)

# Let's do some machine lerning!
connection = sqlite3.connect(db.DATABASE)
c = connection.cursor()
to_id = 1 # Only select the recipient
from_id = 2 # Only select the sender
textsDataFrameTo = pd.read_sql("SELECT * FROM RECIPIENT WHERE type = " + str(to_id) + ";", connection)
textsDataFrameFrom = pd.read_sql("SELECT * FROM RECIPIENT WHERE type = " + str(from_id) + ";", connection)
    
with open('./nmt-chatbot/new_data/train.from','a', encoding='utf8') as f:
    for content in textsDataFrameTo["body"].values:
        f.write(content + '\n')

with open('./nmt-chatbot/new_data/train.to','a', encoding='utf8') as f:
    for content in textsDataFrameFrom["body"].values:
        f.write(content  +'\n')