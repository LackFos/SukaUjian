from Database.Connect import Connect

class soal:
    def __init__(self):
        self.__db = Connect()
    
    def __inputExamId(self):
        # Dapatkan id exam
        print("\nPilih matakuliah\n")
        print("1. Matematika\n2. Bahasa Indonesia\n3. Mandarin")
        return input("\nMasukkan id nomor matakuliah : ")

    def __printTable(self, data):
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


    def tambahSoal(self):
        # Dapatkan id exam
        examId = self.__inputExamId()

        # Dapatkan soal
        soalBaru = input("Input soal : ")

        # Dapatkan nomor soal terakhir
        nomorSoalTerakhir = self.__db.rawOne(f"SELECT * FROM soal WHERE exam_id = %s ORDER BY nomor DESC LIMIT 1", [examId])["nomor"]

        self.__db.insert("soal", {"exam_id": examId, "nomor": nomorSoalTerakhir + 1, "soal": soalBaru})
        
    def hapusSoal(self):
        # Dapatkan id exam
        examId = self.__inputExamId()

        # print list soal
        listSoal = self.__db.get("soal", {"exam_id": examId})
        self.__printTable(listSoal)

        # Dapatkan nomor soal yang ingin dihapus
        soalBaru = input("\nMasukkan nomor soal yang ingin dihapus : ")


soal = soal()
soal.hapusSoal()