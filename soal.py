from Database.Connect import Connect

class soal:
    def __init__(self):
        self.__db = Connect()
    
    def tambahSoal(self):
        print("\nPilih matakuliah\n")
        print("1. Matematika\n2. Bahasa Indonesia\n3. Mandarin")
        idMatakuliah = input("\nMasukkan id nomor matakuliah : ")

        soal = input("Input soal : ")

        result = self.__db.rawOne(f"SELECT * FROM soal ORDER BY nomor WHERE id = {idMatakuliah} DESC LIMIT 1")
        print(result)
        
soal = soal()
soal.tambahSoal()