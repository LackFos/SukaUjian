#Kelompok 2 
#2232069 Fariz Ajy Putra
#2232025 Kevin
#2232064 Wilsen Lau
#2232067 Jeffrey
#2232024 Vincent Tham
#2232068 Elvis

# class Dosen:
#     def __init__(self, id, name, course,):
#         self.id = id
#         self.name = name
#         self.course = course


#     def enrollkelas(self):
#         list = ("matematika","bahasa Inggirs")
#         for i in range(len(list)):
#             print(f"{i+1}. {list[i]} ")
#         while True:
#             x =input("Silakan masukan nomor kelas : ")
#             if x == "1":
#                 print("kamu telah dimasukan ke kelas Matematika(Dosen)")
#                 break
#             elif x == "2":
#                 print("kamu telah dimasukan ke kelas Bahasa Inggris(Dosen)")
#                 break
#             else :
#                 print("data yang kamu masukan salah silakan isi kembali")

#     def inputnilai(self):
#         list = ("matematika","bahasa Inggirs")
#         for i in range(len(list)):
#             print(f"{i+1}. {list[i]} ")
#         while True:
#             m=input("Nomor Mata Kuliah : ")
#             if m == "1":
#                 m="Matematika"
#                 break
#             elif m == "2":
#                 m="Bahasa Inggris"
#                 break
#             else :
#                 print("Data yang anda masukan salah silakan isi ulang")
#         n=input("Nama Mahasiswa : ")
#         ni=input("Nilai : ")
#         print(f"Nama : {n}\t", f"MataKuliah : {m}\t", f"Nilai : {ni}\t")


# Dosen1 = Dosen("1","Elvis","Bahasa Inggris")
# Dosen2 = Dosen("2","Jeffey","Matematika")

# print(Dosen1._name)
# print(Dosen2.id)
# print(Dosen2.course)

# Dosen2.enrollkelas()
# Dosen1.inputnilai()
import os

class Dosen:
    def __init__(self, id, name, course):
        self.__id = id
        self._name = name
        self.course = course


    def CreateExam(self):
        x=self.course
        print(f"Halo mr/ms {self._name} dengan mata kuliah {self.course}")
        y=input("Silakan masukan tanggal Ujian(DD/MM/YYYY):")
        with open(f'D:\Tugas\Latihan\OOP\Daftar Ujian.txt','a') as f:
            f.write(f'{x} {y},')

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