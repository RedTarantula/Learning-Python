# SQLite included in python

import sqlite3
import os
os.system('clear')

conn = sqlite3.connect('customer.db') # if doesnt exist, python will create it
cursor = conn.cursor() # does stuff in the database

# Data Types
# text
# int
# real
# blob - image, audio, etc
# null or not null

# cursor.execute("""CREATE TABLE customer (
# 			first_name text,
# 			last_name text,
# 			email text
# 			)""")

# cursor.execute("INSERT INTO customer VALUES ('John','Elder','john@faggot.com')")

cursor.execute("SELECT * FROM customer")
print(cursor.fetchall()[0][0])

conn.commit() # commits changes to database




conn.close() # always close the connection