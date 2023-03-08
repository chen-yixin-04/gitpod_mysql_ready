import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO mammiferi (Id, Nome_Proprio, Razza, Peso, Eta) VALUES (%s,%s,%s,%s,%s)"
val = [("1", "gatto","ragdoll",5,10),
       ("2", "cane","barboncino",3,2),
       ("3", "cavia","peruviana",1,3),
       ("4", "criceto","siriano",1,1),
       ("5", "elefante","africano",3,20)
]
mycursor.executemany(sql, val)

mydb.commit()
