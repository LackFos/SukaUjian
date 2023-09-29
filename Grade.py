class grade:
    def __init__(self, mahasiswa, mataKuliah, hasil):
        self.mahasiswa = mahasiswa;
        self.mataKuliah = mataKuliah;
        self.hasil = hasil;
        self.__grade = ""

        if(self.hasil < 20):
            self.grade = "E"
        elif(self.hasil < 40):
            self.grade = "D"
        elif(self.hasil < 60):
            self.grade = "C"
        elif(self.hasil < 80):
            self.grade = "B"
        else:
            self.grade = "A"

    def cetakStatusKelulusan(self):
        if(self.hasil > 80): 
            print(self.mahasiswa, "lulus dalam matakuliah", self.mataKuliah)
        else:
            print(self.mahasiswa, "tidak lulus dalam matakuliah", self.mataKuliah)
        
    def cetakHasil(self):
        print(self.mahasiswa, "medapatkan", self.grade, "dalam matakuliah", self.mataKuliah)

grade_1 = grade("Fariz", "MTK", 19)
grade_1.__grade = False
grade_1.cetakHasil()

# Perubahan