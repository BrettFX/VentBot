import sqlite3
import DataNormalizer as dn


sql_transaction = []
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
    c.execute("""CREATE TABLE RECIPIENT (text_id INT PRIMARY KEY, phone TEXT, type TEXT, subject TEXT, ,body TEXT)""")
    return


# Format of normalizedData: [{phoneKey : phoneValue, typeKey : typeValue, subjectKey, subjectValue, bodyKey, bodyValue}, ... ]
# Iterate: 
#   for dataRow in normalizedData:
#       for data in dataRow:
#           Processing here
def create(normalizedData):
	create_table()
	ins_query = ""



	for i in normalizedData:
			# i[dn.PHONE_KEY]
		phone = str(i[dn.PHONE_KEY])
		t_ype = str(i[dn.TYPE_KEY])
		sub = str(i[dn.SUBJECT_KEY])
		bod = str(i[dn.BODY_VALUE])
		c.execute("INSERT INTO RECIPIENT VALUES (" + phone + ", " + t_ype + ", " + sub + ", " +  bod + ")")
	return

def transaction_bld(sql):
	sql_transaction.append(sql)
	if len(sql_transactionql)  > TRANS_MAX:
		c.execute("BEGIN TRANSACTION")
		for i in sql_transaction:
			try:
				c.execute(i)
			except:
				pass
		connection.commit()
		sql_transaction = []


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

# Run the program
run()