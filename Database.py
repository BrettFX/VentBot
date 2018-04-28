import sqlite3

sql_transaction = []

connection = sqlite3.connect('{}.db')

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
    
    if __name__ == "__main__":
        create_table()

def insert_row():
    c.execute("INSERT INTO RECIPIENT ")
    
# Format of normalizedData: [{phoneKey : phoneValue, typeKey : typeValue, subjectKey, subjectValue, bodyKey, bodyValue}, ... ]
# Iterate: 
#   for dataRow in normalizedData:
#       for data in dataRow:
#           Processing here
def create(normalizedData):
    return
    
def run():
    return

# Run the program
run()