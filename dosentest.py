import mysql.connector

mydb = mysql.connector.connect(
    user="root", 
    password="",
    host="127.0.0.1",
    database="jadwal_ujian"
    )
if mydb.is_connected():
    print("Database Berhasil Terkoneksi")


cursor = mydb.cursor()
sql = "SELECT * FROM `waktu ujian`"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)