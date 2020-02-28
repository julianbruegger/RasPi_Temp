import mysql.connector

mydb = mysql.connector.connect(
  host="10.20.11.199",
  user="root",
  passwd="123ict",
  database="temp_data"
)

mycursor = mydb.cursor()
print('Whats the Tablename')
tablename = input()
mycursor.execute("CREATE TABLE (tablename) name VARCHAR(255), address VARCHAR(255))")