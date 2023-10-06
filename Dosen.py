
import mysql.connector
from Database.Connect import Connect

class Dosen:
    def __init__(self):
        self.db =Connect()


    def login(self, id):
        result = self.db.get('dosen', {"id": id})
        self.nama = result.get('Name')

    def CreateExam(self,id):
            result = self.db.get('dosen', {"id": id})
            self.nama = result.get('Name')
            self.course = result.get('Courses')
            print(f"Halo mr/ms {self.nama} dengan mata kuliah {self.course}")
            y=input("Silakan masukan tanggal Ujian(YYYY-MM-DD):")
            x=input("Silakan masukan Jam Ujian(HH:MM-HH:MM):")
            self.db.insert("ujian", {"ID":"Null", "Nama Dosen": f"{self.nama}","MataKuliah": f"{self.course}","Jam": f"{x}","Tanggal": f"{y}"})
            self.db.__execute()

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
Dosen1.CreateExam(3)
