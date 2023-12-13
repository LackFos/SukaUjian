from Database.Connect import Connect

class grade:
    def __init__(self):
        self.db = Connect()

    def cetakStatusKelulusan(self):
        if(self.hasil > 80): 
            print(self.mahasiswa, "lulus dalam matakuliah", self.mataKuliah)
        else:
            print(self.mahasiswa, "tidak lulus dalam matakuliah", self.mataKuliah)
        
    def cetakHasil(self):
        print(self.mahasiswa, "medapatkan", self.grade, "dalam matakuliah", self.mataKuliah)

grade_1 = grade()
