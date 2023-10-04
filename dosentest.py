import os
import mysql.connector

class Dosen:
    def __init__(self):
        __mydb= None
        __cursor=None
        try:
            self.__mydb=mysql.connector.connect(
                user="root", 
                password="",
                host="127.0.0.1",
                database="dosen_python"
                )
            if self.__mydb.is_connected():
                print("Database Berhasil Terkoneksi")
        except:
            print("Database Gagal Terkoneksi")

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
            print(f"{results[i]}")

    def DeleteExam(self):
        while True :
            x=input(f"Halo mr/ms {self._name} apakah anda yakin untuk menghapus daftar ujian?(Y/N): ").upper()
            if x == "Y":
                os.remove(f'D:\Tugas\Latihan\OOP\Daftar Ujian.txt')
                break
            elif x == "N":
                break
            else:
                print("Data eror silakan masukan data anda kembali")
            
    def Showname(self):
        print(self.__id)



Dosen1 = 
Dosen2.DisplayExam()