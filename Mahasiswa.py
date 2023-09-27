
class Mahasiswa: 
    def __init__(self, npm, nama, matakuliah, jumlahsks):
        self.__nama = nama
        self.__npm = npm
        self.matakuliah = matakuliah
        self._jumlahsks = jumlahsks
       

    def enroll_kelas(self):
        return f"{self.__nama} dengan npm {self.__npm} sedang enroll matakuliah {self.matakuliah} dengan jumlah sks {self._jumlahsks} "

    def take_exam(self):
        return f"{self.__nama} dengan npm {self.__npm} mengambil ujian {self.matakuliah}"

mahasiswa1 = Mahasiswa(2232025, "kevin", "Mandarin",3)

print (mahasiswa1.enroll_kelas()) 
print (mahasiswa1.take_exam())

#class Child(Mahasiswa):  
#    def __init__(self, npm, nama, takeexam, nilai):
#        super().__init__(npm, nama, takeexam)
#        self.nilai = nilai

#mahasiswa2 = Child(2232024, "rick", "matematika", 80)
#mahasiswa2.enroll_ujian() 
#mahasiswa2.kumpul_ujian()

#print(mahasiswa2._takeexam)

