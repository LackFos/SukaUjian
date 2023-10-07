import mysql.connector
from Database.Connect import Connect

class Dosen:
    def __init__(self,id):
        self.db=Connect()
        result=self.db.get('dosen', {"id": id})
        self.id=result.get("ID")
        self.name=result.get("Name")
        self.courses=result.get("Courses")

    def ExamSchedule(self):
        print(f"Halo MR/MRS {self.name}")
        Date=input("Silakan masukan tanggal ujian(YYYY-MM-DD): ")
        Time=input("Silakan masukan Waktu ujian(HH:MM-HH:MM): ")
        self.db.insert(
            'Ujian',
            {"ID":"Null", 
            "NamaDosen":f"{self.name}",
            "MataKuliah":f"{self.courses}",
            "Jam":f"{Time}",
            "Tanggal":f"{Date}"}
            )
        
    def DisplayExam(self):
        x=self.db.select("ujian")
        for i in range(len(x)):
            print(f"{i+1}. {x[i]}")

    def UpdateExam(self):
        self.DisplayExam()
        print(f"Halo MR/MRS {self.name}, Silakan melakukan perubahan jadwal dimohon untuk tidak mengaganngu jadwal dosen lain")
        x=input("Silakan masukan ID: ")
        Date=input("Silakan masukan tanggal ujian(YYYY-MM-DD): ")
        Time=input("Silakan masukan Waktu ujian(HH:MM-HH:MM): ")
        self.db.update(
            "ujian",
            {"ID":f"{x}"},
            {"Jam":f"{Time}",
            "Tanggal":f"{Date}"}
        )

    def DeleteExam(self):
        self.DisplayExam()
        print(f"Halo MR/MRS {self.name}, Silakan melakukan penghapusan jadwal dimohon untuk tidak mengaganngu jadwal dosen lain")
        x=input("Silakan masukan ID: ")
        self.db.delete("ujian",{"ID":f"{x}"})







dosen1=Dosen(2)
dosen1.DeleteExam()