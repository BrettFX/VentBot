# Driver Program

import Database as db
import DataNormalizer as dn
import sqlite3

DATA = "./data/Jack_Test1.xml"

normalizedData = dn.parseXML(DATA)
db.create(normalizedData)
print(db.query(1, "body"))

# Let's do some machine lerning!
connection = sqlite3.connect(db.DATABASE)
c = connection.cursor()
t_id = 1 # Only select the recipient
textsDataFrame = pd.read_sql("SELECT * FROM RECIPIENT WHERE type = " + str(t_id) + ";", connection)

numTests = int(len(textsDataFrame) / 2)
numTrains = int(len(textsDataFrame) - numTests)

# Create training sets and test sets (N-fold cross validation where N = 2)
trainData = textsDataFrame[0:numTrains]
testData = textsDataFrame[numTrains : int(len(textsDataFrame))]
    
with open('test.from','a', encoding='utf8') as f:
    for content in trainData["body"].values:
        f.write(content + '\n')

with open('test.to','a', encoding='utf8') as f:
    for content in testData["body"].values:
        f.write(content  +'\n')