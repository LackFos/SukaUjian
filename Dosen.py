import os

class Dosen:
    def __init__(self, id, name, course):
        self.__id = id
        self._name = name
        self.course = course


    def CreateExam(self):
        try:
            mydb = mysql.connector.connect(
            user="root", 
            password="",
            host="127.0.0.1",
            database="jadwal_ujian"
            )
            if mydb.is_connected():
                print("Database Berhasil Terkonelsi")
                print(f"Halo mr/ms {self._name} dengan mata kuliah {self.course}")
                y=input("Silakan masukan tanggal Ujian(YYYY-MM-DD):")
                x=input("Silakan masukan Jam Ujian(HH:MM-HH:MM):")
                cursor = mydb.cursor()
                sql = "INSERT INTO `waktu ujian` (`ID`, `Jam`, `Tanggal`, `MataKuliah`) VALUES (Null, %s,%s,%s);"
                val = (f"{x}",f"{y}",f"{self.course}")
                cursor.execute(sql, val)
                mydb.commit()
                print("Data Ditambahkan")

        except:
            print("Database Gagal Terkoneksi")


    def DisplayExam(self):
        print(f"Halo mr/ms {self._name} berikut daftar ujian" )
        with open(f'D:\Tugas\Latihan\OOP\Daftar Ujian.txt','r') as f:
            a=f.read()
        x=len(a)
        y=a[:x-1]
        list=y.split(",")
        for i in range(len(list)):
            print(f"{i+1}. {list[i]}")

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



Dosen1 = Dosen("1","Elvis","Bahasa Inggris")
Dosen2 = Dosen("2","Jeffey","Matematika")

Dosen2.CreateExam()
