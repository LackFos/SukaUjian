from Database.Connect import Connect

conn = Connect()

class Answer:
    def __init__(self):
        # Meminta pengguna memasukkan token
        token = input("Masukkan token: ")

        # Periksa apakah token sesuai dengan yang diharapkan
        if token == "test": 
            self.run_program()
        else:
            print("Token tidak valid. Aplikasi akan keluar.")

    def run_program(self):
        while True:
            print("Pilih salah satu tindakan:")
            print("1. Simpan Jawaban")
            print("2. Delete Jawaban")
            print("3. Update Jawaban")
            print("4. Tampilkan Jawaban")
            print("5. Keluar")
            
            choice = input("Pilih tindakan Anda (1/2/3/4/5): ")

            if choice == "1":
                print("Pilih salah satu jawaban: a, b, c, atau d")
                pilihan = input("Jawaban Anda: ")
                nomor = int(input("Nomor mahasiswa: "))

                if pilihan in ['a', 'b', 'c', 'd']:
                    nama = input("Masukkan nama mahasiswa: ")
                    jawaban = pilihan
                    self.nama = nama
                    self.nomor = nomor
                    self.jawaban = jawaban
                    self.simpan_jawaban()
                    print("Anda memilih:", pilihan)
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

            elif choice == "2":
                nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
                nomor = input("Nomor mahasiswa: ")
                self.nama = nama
                self.nomor = nomor
                self.delete_jawaban()
                print("Data mahasiswa dengan nama {} dan nomor {} telah dihapus.".format(nama, nomor))

            elif choice == "3":
                nama = input("Masukkan nama mahasiswa yang ingin diupdate: ")
                nomor = int(input("Nomor mahasiswa: "))
                pilihan = input("Jawaban baru: ")
                self.nama = nama
                self.nomor = nomor 
                self.jawaban = pilihan
                self.update_jawaban()
                print("Data mahasiswa dengan nama {} dan nomor {} telah diupdate.".format(nama, nomor))

            elif choice == "4":
                nama = input("Masukkan nama Mahasiswa yang: ")
                self.nama = nama
                self.tampilin_jawaban()

            elif choice == "5":
                print("Terima kasih! Program berakhir.")
                break

            else:
                print("Tindakan tidak valid. Silakan coba lagi.")

    def simpan_jawaban(self):
        conn.insert("mahasiswa", {"nama": self.nama, "nomor": self.nomor, "jawaban": self.jawaban})

    def delete_jawaban(self):
        conn.delete("mahasiswa", {"nama": self.nama, "nomor": self.nomor})

    def update_jawaban(self):
        conn.update("mahasiswa", {"nama": self.nama, "nomor": self.nomor}, {"jawaban": self.jawaban})
    
    def tampilin_jawaban(self):
        data = conn.get("mahasiswa", {"nama": self.nama},["nama", "jawaban"])
        for row in data:
            print("Nama:", row["nama"], "Jawaban:", row["jawaban"])

Answer() 