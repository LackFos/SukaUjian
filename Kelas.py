class Kelas:
    def __init__(self, nomor, capacity, occupied, ac=False):
        self.__nomor = nomor
        self.__capacity = capacity
        self.__occupied = occupied
        self.__ac = ac

    def pinjamKelas(self, banyakMahasiswa):
        if self.__occupied:
            print("Kelas", self.__nomor, "ini sudah dipakai")
            return

        if banyakMahasiswa > self.__capacity:
            print("Kelas", self.__nomor, "ini tidak muat")
        else:
            print("Kelas", self.__nomor, "ini berhasil dipinjam")
            self.__occupied = True

    def kembalikanKelas(self):
        self.__occupied = False

    def ada_ac(self):
        if self.__ac:
            return "Ada"
        else:
            return "Tiada"

# Create instances of Kelas for multiple classrooms
kelas_list = [
    Kelas("315", 30, False, ac=True),
    Kelas("316", 25, False, ac=False),
    Kelas("317", 35, False, ac=True),
    Kelas("318", 40, False, ac=True),
    Kelas("319", 20, False, ac=False),
    Kelas("320", 30, True, ac=True),
    Kelas("321", 25, False, ac=False),
    Kelas("322", 35, False, ac=True),
    Kelas("323", 40, True, ac=True),
    Kelas("324", 20, False, ac=False),
    Kelas("325", 30, False, ac=True),
    # Add more classrooms here
]

# Example usage
for kelas in kelas_list:
    kelas.pinjamKelas(30)
    kelas.kembalikanKelas()
    print("Kelas", kelas._Kelas__nomor, "ada air conditioner:", kelas.ada_ac())

