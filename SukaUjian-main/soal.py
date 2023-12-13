from Database.Connect import Connect

class soal:
    def __init__(self, id, ):
        self.__id = id
        self.__db = Connect()

    def mulai(self):
        query = f"""
            SELECT soal, kunci_jawaban, pilihan_1, pilihan_2, pilihan_3, pilihan_4 
            FROM soal_jawaban 
            INNER JOIN soal ON soal_jawaban.soal_id = soal.id 
            WHERE soal.exam_id IN ({self.__id})
            ORDER BY RAND()"""

        result = self.__db.raw(query)

        if result :
            for soal in result:
                print("")
                print(soal['soal'])
                print('a. ', soal['pilihan_1'])
                print('b. ', soal['pilihan_2'])
                print('c. ', soal['pilihan_3'])
                print('d. ', soal['pilihan_4'])
                jawaban = input("\nPilih jawabanmu : ")
                print("Anda benar") if jawaban == result[0]['kunci_jawaban'] else print("Anda Salah")
        else:
            print("Belum ada soal")        

    def __getPilihan(self, soalId):
        listPilihan = self.__db.get("soal_jawaban", {"soal_id": soalId}, ["soal_id", "pilihan_1", "pilihan_2", "pilihan_3", "pilihan_4"])
        self.__printTable(listPilihan)
        self.__updatePilihan(listPilihan[0]["soal_id"])

class soal_mtk(soal):
    def __init__(self, id, mataKuliah):
        super().__init__(id)
        self.mataKuliah = mataKuliah

class soal_pbo(soal):
    def __init__(self, id, mataKuliah):
        super().__init__(id)
        self.mataKuliah = mataKuliah


soal_mtk = soal_mtk(1, "MTK")
print(f"Anda mengerjakan soal {soal_mtk.mataKuliah}")
soal_mtk.mulai()
print(f"Ujian Selesai {soal_mtk.mataKuliah}\n")

soal_pbo = soal_pbo(2, "PBO")
print(f"Anda mengerjakan soal {soal_pbo.mataKuliah}")
soal_pbo.mulai()
print(f"Ujian Selesai {soal_pbo.mataKuliah}\n")


# Di comment sementara karena fitur admin belum dibtuuhkan untuk mengerjakan soal ini 

        # if self.__isAdmin :
        #     print("\n1. Tambah Soal\n2. Edit Soal\n3. Hapus Soal")
        #     opsiTerpilih = input("\nMasukkan pilihanmu : ")
            
        #     if opsiTerpilih == "1":
        #         examId = self.__getExamId()
        #         soal = input("Masukkan soal : ")
        #         soalId = self.tambahSoal(examId, soal)
        #         self.__tambahPilihan(soalId)
        #         self.__setKunciJawaban(soalId)

        #     elif opsiTerpilih == "2":
        #         examId = self.__getExamId()
        #         nomorSoal = self.__getNomorSoal(examId)
        #         opsiTerpilih = input("\n1. Edit Soal\n2. Edit Pilihan\nPilih opsi : ")

        #         if opsiTerpilih == "1":
        #             soal = input("Masukkan soal baru : ")
        #             self.__db.update("soal", {"exam_id": examId, "nomor": nomorSoal}, {"soal": soal})
        #         elif opsiTerpilih == "2":
        #             soalId = self.__db.first("soal", {"exam_id": examId, "nomor": nomorSoal}, ["id"])["id"]
        #             self.__getPilihan(soalId)
                    
        #     elif opsiTerpilih == "3":          
        #         examId = self.__getExamId()
        #         nomorSoal = self.__getNomorSoal(examId)
        #         self.hapusSoal(examId, nomorSoal)

        #     else:
        #         print("Opsi yang dipilih tidak valid")

        # else :


    #        def tambahSoal(self, examId, soal):
    #     isFirstRow = self.__db.rawOne("SELECT MAX(nomor) as nomor_terakhir FROM soal")["nomor_terakhir"]
    #     nomorTerakhir = 1 if isFirstRow == None else isFirstRow + 1
    #     self.__db.insert("soal", {"exam_id": examId, "nomor": nomorTerakhir, "soal": soal})
    #     return nomorTerakhir

    # def editSoal(self, examId, nomorSoal, soal):
    #     return self.__db.update("soal", {"exam_id": examId, "nomor": nomorSoal}, {"soal": soal})
        
    # def hapusSoal(self, examId, nomorSoal): 
    #     return self.__db.delete("soal", {"exam_id": examId, "nomor": nomorSoal})

    # def __getExamId(self):
    #     print("\n1. Bahasa Indonesia\n2. Bahasa Inggris\n3. Bahasa Mandarin")
    #     return input("\nPilih sesi ujian : ")

    # def __getNomorSoal(self, examId):
    #     listSoal = self.__db.get("soal", {"exam_id": examId}, ["nomor", "soal"])
    #     self.__printTable(listSoal)
    #     return input("\nMasukkan nomor soal : ")

    # def __tambahPilihan(self, soalId):
    #     pilihan_1 = input("\npilihan A : ")
    #     pilihan_2 = input("pilihan B : ")
    #     pilihan_3 = input("pilihan C : ")
    #     pilihan_4 = input("pilihan D : ")
    #     self.__db.insert("soal_jawaban", {"soal_id": soalId, "pilihan_1": pilihan_1, "pilihan_2": pilihan_2, "pilihan_3": pilihan_3, "pilihan_4": pilihan_4})

    # def __updatePilihan(self, soalId):
    #     pilihan_1 = input("\npilihan A : ")
    #     pilihan_2 = input("pilihan B : ")
    #     pilihan_3 = input("pilihan C : ")
    #     pilihan_4 = input("pilihan D : ")
    #     self.__db.update("soal_jawaban", {"soal_id": soalId}, {"pilihan_1": pilihan_1, "pilihan_2": pilihan_2, "pilihan_3": pilihan_3, "pilihan_4": pilihan_4})

    # def __setKunciJawaban(self, soalId):
    #     kunciJawaban = input("Masukkan jawaban soal ini : ")
    #     self.__db.update("soal", {"id": soalId}, {"kunci_jawaban": kunciJawaban})

    # def __printTable(self, data):
    #     if(len(data) == 0):
    #         print("\nTidak ada soal pada exam yang dipilih")
    #         return False;

    #     headers = data[0].keys()

    #     column_widths = {header: len(str(header)) for header in headers}
    #     for row in data:
    #         for header, value in row.items():
    #             column_widths[header] = max(column_widths[header], len(str(value)))
    #     print("\n")
    #     print("|".join(f"{header:<{column_widths[header]}}" for header in headers))
    #     print("-" * (sum(column_widths.values()) + len(headers) - 1))

    #     for row in data:
    #         print("|".join(f"{str(row[header]):<{column_widths[header]}}" for header in headers))

