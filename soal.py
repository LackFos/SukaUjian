from Database.Connect import Connect

class soal:
    def __init__(self):
        self.__db = Connect()
    
    def __inputExamId(self):
        # Dapatkan id exam
        print("\nPilih exam\n")
        print("1. Matematika\n2. Bahasa Indonesia\n3. Mandarin")
        return input("\nMasukkan id nomor matakuliah : ")

    def __printTable(self, data):
        if(len(data) == 0):
            print("\nTidak ada soal pada exam yang dipilih")
            return False;

        headers = data[0].keys()

        column_widths = {header: len(str(header)) for header in headers}
        for row in data:
            for header, value in row.items():
                column_widths[header] = max(column_widths[header], len(str(value)))
        print("\n")
        print("|".join(f"{header:<{column_widths[header]}}" for header in headers))
        print("-" * (sum(column_widths.values()) + len(headers) - 1))

        for row in data:
            print("|".join(f"{str(row[header]):<{column_widths[header]}}" for header in headers))

        return True

    def tambahSoal(self):
        soalTidakKosong = self.dapatkanSoal()

        if(not soalTidakKosong):
            return

        # Dapatkan nomor soal terakhir
        soalTerakhir = self.__db.rawOne(f"SELECT * FROM soal WHERE exam_id = %s ORDER BY nomor DESC LIMIT 1", [self.examId])
        nomorSoal = nomorSoalTerakhir["nomor"] + 1 if soalTerakhir else 1

        self.__db.insert("soal", {"exam_id": self.examId, "nomor": nomorSoal, "soal": soalBaru})
        
    def hapusSoal(self):
        soalTidakKosong = self.dapatkanSoal()

        if(not soalTidakKosong):
            return

        # Dapatkan nomor soal yang ingin dihapus
        nomorSoal = input("\nMasukkan nomor soal yang ingin dihapus : ")

        self.__db.delete("soal", {"exam_id": self.examId, "nomor": nomorSoal})

    def editSoal(self):
        soalTidakKosong = self.dapatkanSoal()

        if(not soalTidakKosong):
            return

        # Dapatkan nomor soal yang ingin dihapus
        nomorSoal = input("\nMasukkan nomor soal yang ingin diganti : ")
        soalBaru = input("\nInput soal baru : ")
        self.__db.update("soal", {"exam_id": self.examId, "nomor": nomorSoal}, {"soal": soalBaru})

    def dapatkanSoal(self, isRandom=False):
        self.examId = self.__inputExamId()

        # print list soal
        listSoal = self.__db.get("soal", {"exam_id": self.examId}, ["soal"]) if not isRandom else self.__db.raw("SELECT soal FROM soal ORDER BY RAND()")
        return self.__printTable(listSoal)


soal = soal()
soal.dapatkanSoal(True)