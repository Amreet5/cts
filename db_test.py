import sqlite3
import datetime

connection = sqlite3.connect("CTS.db")
cursor = connection.cursor()
t = '11/21/19'
y = '11/23/19'
cursor.execute('SELECT * from CTS')# where Date BETWEEN ? AND ?', (t,y))
result = cursor.fetchall()

for i in result:
 print(i) 



