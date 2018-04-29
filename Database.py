import sqlite3
import DataNormalizer as dn

TRANS_MAX = 100

connection = sqlite3.connect('Texts.db')

c = connection.cursor()

# Columns: phone, type, subject, body
# Data Format:
# dataRow = {phoneKey : phoneValue, typeKey : typeValue, subjectKey, subjectValue, bodyKey, bodyValue}
# Access element when key is known: dataRow["PhoneKey"]
# Access elements in dataRow without known key:
# for data in dataRow:
#   dataRow[data]
def create_table():
	# c.execute("DROP TABLE RECIPIENT;")
	c.execute("""CREATE TABLE IF NOT EXISTS RECIPIENT (text_id INT PRIMARY KEY, phone TEXT, type TEXT, subject TEXT, body TEXT);""")
	return

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
			# i[dn.PHONE_KEY]
		phone = str(i[dn.PHONE_KEY])
		t_ype = str(i[dn.TYPE_KEY])
		sub = str(i[dn.SUBJECT_KEY])
		bod = str(i[dn.BODY_KEY])

		c.execute("INSERT INTO RECIPIENT (phone, type, subject, body) VALUES ({}, {}, {}, {})".format(phone, t_ype, sub, bod))
		# transaction_bld("INSERT INTO RECIPIENT VALUES (" + phone + ", " + t_ype + ", " + sub + ", " +  bod + ")", sql_transaction)
	return




def show_row(t_id):
	try:
		c.execute("SELECT * FROM RECIPIENT WHERE text_id = " + t_id + ";")
		result = c.fetchone()
		if result != None:
			return result[0]
		else: 
			return False
	except Exception as e:
		return False
    
def run():
    return