import os
import mysql.connector
from Database.Connect import Connect

class Dosen:
    def __init__(self):
        self.db = Connect()


    def login(self, id):
        result = self.db.get('dosen', {"id": id})
        self.nama = result.get('Name')

    def CreateExam(self):
        try:
            mydb = mysql.connector.connect(
            user="root", 
            password="",
            host="127.0.0.1",
            database="jadwal_ujian"
            )
            if mydb.is_connected():
                print("Database Berhasil Terkoneksi")
                print(f"Halo mr/ms {self._name} dengan mata kuliah {self.course}")
                y=input("Silakan masukan tanggal Ujian(YYYY-MM-DD):")
                x=input("Silakan masukan Jam Ujian(HH:MM-HH:MM):")
                cursor = mydb.cursor()
                sql = "INSERT INTO `waktu ujian` (`ID`,`Nama Dosen`, `MataKuliah`, `Jam`, `Tanggal`) VALUES (Null,%s, %s,%s,%s);"
                val = (f"{self._name}",f"{self.course}",f"{x}",f"{y}")
                cursor.execute(sql, val)
                mydb.commit()
                print("Data Ditambahkan")

        except:
            print("Database Gagal Terkoneksi")


    def DisplayExam(self):
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

        for i in range(len(results)):
            print(f"{i+1}. {results[i]}")

    def DeleteExam(self):
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

            for i in range(len(results)):
                print(f"{i+1}. {results[i]}")
            x = input("Silakan Masukan ID yang ingin dihapus: ")
            cursor = mydb.cursor()
            sql = "DELETE FROM `waktu ujian` WHERE ID=%s;"
            val = [f"{x}"]
            cursor.execute(sql, val)
            mydb.commit()
            print("{} data dihapus".format(cursor.rowcount))


    def Showname(self):
        print(self.__id)



Dosen1 = Dosen()
Dosen1.login(3)
print(Dosen1.nama)