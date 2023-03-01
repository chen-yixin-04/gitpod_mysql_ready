import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE mammiferi (Id int(200), Nome_Proprio VARCHAR(200), Razza VARCHAR(200), Peso int(200), Eta int(200))")
