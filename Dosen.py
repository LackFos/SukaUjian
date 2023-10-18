import mysql.connector
from Database.Connect import Connect

class Dosen:
    def __init__(self,id):
        self.db=Connect()
        Result=self.db.first('dosen',{"ID":id})
        self.id=Result["ID"]
        self.nama=Result["NAMA"]
        self.matakuliah=Result["MATAKULIAH"]

    def ExamSchedule(self):
        print(f"Halo MR/MRS {self.nama}")
        Date=input("Silakan masukan tanggal ujian(YYYY-MM-DD): ")
        Time=input("Silakan masukan Waktu ujian(HH:MM-HH:MM): ")
        self.db.insert(
            'jadwal',
            {"ID":"Null", 
            "DOSEN":f"{self.nama}",
            "MATAKULIAH":f"{self.matakuliah}",
            "JAM":f"{Time}",
            "TANGGAL":f"{Date}"}
            )
        

        
    def DisplayExam(self):
        x=self.db.select("jadwal")
        for i in range(len(x)):
            print(f"{i+1}. {x[i]}")


    def UpdateExam(self):
        self.DisplayExam()
        print(f"Halo MR/MRS {self.nama}, Silakan melakukan perubahan jadwal dimohon untuk tidak mengaganngu jadwal dosen lain")
        x=input("Silakan masukan ID: ")
        Date=input("Silakan masukan tanggal ujian(YYYY-MM-DD): ")
        Time=input("Silakan masukan Waktu ujian(HH:MM-HH:MM): ")
        self.db.update(
            "jadwal",
            {"ID":f"{x}"},
            {"JAM":f"{Time}",
            "TANGGAL":f"{Date}"}
        )

    def DeleteExam(self):
        self.DisplayExam()
        print(f"Halo MR/MRS {self.nama}, Silakan melakukan penghapusan jadwal dimohon untuk tidak mengaganngu jadwal dosen lain")
        x=input("Silakan masukan ID: ")
        self.db.delete("jadwal",{"ID":f"{x}"})



dosen1=Dosen(1)
dosen2=Dosen(2)
dosen1.ExamSchedule()
dosen2.ExamSchedule()

#dosen1.DisplayExam()
#dosen1.UpdateExam()
#dosen1.DeleteExam()