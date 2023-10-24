import mysql.connector
from Database.Connect import Connect

class Jadwal:
    def __init__(self,id):
        self.__db=Connect()
        Result=self.__db.first('dosen',{"ID":id})
        self.__id=Result["ID"]
        self.nama=Result["NAMA"]
        self.matakuliah=Result["MATAKULIAH"]

    def ExamSchedule(self):
        print(f"Halo MR/MRS {self.nama}")
        Date=input("Silakan masukan tanggal ujian(YYYY-MM-DD): ")
        Time=input("Silakan masukan Waktu ujian(HH:MM-HH:MM): ")
        self.__db.insert(
            'jadwal',
            {"ID":"Null", 
            "DOSEN":f"{self.nama}",
            "MATAKULIAH":f"{self.matakuliah}",
            "JAM":f"{Time}",
            "TANGGAL":f"{Date}"}
            )
        

        
    def DisplayExam(self):
        x=self.__db.select("jadwal")
        for i in range(len(x)):
            print(f"{i+1}. {x[i]}")


    def UpdateExam(self):
        self.DisplayExam()
        print(f"Halo MR/MRS {self.nama}, Silakan melakukan perubahan jadwal dimohon untuk tidak mengaganngu jadwal dosen lain")
        x=input("Silakan masukan ID: ")
        Date=input("Silakan masukan tanggal ujian(YYYY-MM-DD): ")
        Time=input("Silakan masukan Waktu ujian(HH:MM-HH:MM): ")
        self.__db.update(
            "jadwal",
            {"ID":f"{x}"},
            {"JAM":f"{Time}",
            "TANGGAL":f"{Date}"}
        )

    def DeleteExam(self):
        self.DisplayExam()
        print(f"Halo MR/MRS {self.nama}, Silakan melakukan penghapusan jadwal dimohon untuk tidak mengaganngu jadwal dosen lain")
        x=input("Silakan masukan ID: ")
        self.__db.delete("jadwal",{"ID":f"{x}"})

while True:
    try:
        id=input("Silakan masukan id dosen: ")
        dosen=Jadwal(id)
        break
    except:
        print("Input eror masukan id dosen dengan benar")

while True:
    y=["Buat Jadwal","Update Jadwal", "Melihat Jadwal", "Hapus Jadwal", "Keluar"]
    for i in range(len(y)):
        print(f"{i+1}. {y[i]}")
    x=input(f"Halo mr/mrs {dosen.nama} silakan masukan input nomor: ")
    if x == "1":
        dosen.ExamSchedule()
    elif x == "2":
        dosen.UpdateExam()
    elif x == "3":
        dosen.DisplayExam()
    elif x == "4":
        dosen.DeleteExam()
    elif x == "5":
        print("Terimakasih")
        break
    else:
        print("Input eror silakan masukan ulang")


