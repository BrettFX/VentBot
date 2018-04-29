import sqlite3
import DataNormalizer as dn

TRANS_MAX = 100
DATABASE = 'Texts.db'

connection = sqlite3.connect(DATABASE)
c = connection.cursor()

# Columns: phone, type, subject, body
# Data Format:
# dataRow = {phoneKey : phoneValue, typeKey : typeValue, subjectKey, subjectValue, bodyKey, bodyValue}
# Access element when key is known: dataRow["PhoneKey"]
# Access elements in dataRow without known key:
# for data in dataRow:
#   dataRow[data]
def create_table():
	c.execute("DROP TABLE RECIPIENT;")
	c.execute("CREATE TABLE IF NOT EXISTS RECIPIENT (text_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, phone TEXT, type TEXT, subject TEXT, body BLOB);")

def transaction_bld(query, sql_transaction):
	sql_transaction.append(query)
	if len(sql_transaction)  > TRANS_MAX:
		c.execute("BEGIN TRANSACTION")
		for i in sql_transaction:
			try:
				c.execute(i)
			except:
				pass
		connection.commit()
		sql_transaction = []

# Format of normalizedData: [{phoneKey : phoneValue, typeKey : typeValue, subjectKey, subjectValue, bodyKey, bodyValue}, ... ]
# Iterate: 
#   for dataRow in normalizedData:
#       for data in dataRow:
#           Processing here
def create(normalizedData):
	sql_transaction = []

	create_table()

	for i in normalizedData:
		msgPhone = "\'" + str(i[dn.PHONE_KEY]) + "\'"
		msgType = "\'" + str(i[dn.TYPE_KEY]) + "\'"
		msgSubject = "\'" + str(i[dn.SUBJECT_KEY]) + "\'"
		msgBody = "\"" + str(i[dn.BODY_KEY]) + "\""

		# Only parse texts that are in unicode
		try:
			c.execute("INSERT INTO RECIPIENT (phone, type, subject, body) VALUES ({}, {}, {}, {})".format(msgPhone, msgType, msgSubject, msgBody))
		except UnicodeEncodeError:
			c.execute("INSERT INTO RECIPIENT (phone, type, subject, body) VALUES ({}, {}, {}, {})".format(msgPhone, msgType, msgSubject, "\'PARSE ERROR\'"))

	connection.commit()

def show_row(t_id, selector):
	try:
		c.execute("SELECT " + str(selector) + " FROM RECIPIENT WHERE text_id = " + str(t_id) + ";")
		result = c.fetchone()
		if result != None:
			return result
		else: 
			return None
	except Exception as e:
		return None
    
def run():
    return