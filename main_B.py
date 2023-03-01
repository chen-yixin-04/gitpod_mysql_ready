import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

sql = "INSERT INTO mammiferi (Id, Nome_Proprio, Razza, Peso, Eta) VALUES (%s,%s,%s,%s,%s)"
val = [("1", "gatto","ragdoll","5 kg","10")
       ("2", "cane","barboncino","3 kg","2")
       ("3", "cavia","peruviana","1 kg","3")
       ("4", "criceto","siriano","0.5 kg","1")
       ("5", "elefante","africano","3000 kg","20")
]