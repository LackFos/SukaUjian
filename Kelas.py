from Database.Connect import Connect

class Kelas:
    def __init__(self, nomor, capacity, occupied):
        self.__nomor = nomor
        self.__capacity = capacity
        self.__occupied = occupied == 'True'

    # Getter methods
    def get_nomor(self):
        return self.__nomor

    def get_capacity(self):
        return self.__capacity

    def is_occupied(self):
        return self.__occupied

    # Setter methods
    def set_nomor(self, nomor):
        self.__nomor = nomor

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def set_occupied(self, occupied):
        self.__occupied = occupied

    def pinjamKelas(self, banyakMahasiswa):
        if self.__occupied:
            print(f"Kelas {self.__nomor} ini sudah dipakai")
            return

        if banyakMahasiswa > self.__capacity:
            print(f"Kelas {self.__nomor} ini tidak muat")
        else:
            print(f"Kelas {self.__nomor} ini berhasil dipinjam")
            self.__occupied = False

    def kembalikanKelas(self):
        self.__occupied = False

kelas_list = []

db = Connect()
result= db.insert( "kelas2", {15, '329', 45, "False"})
print(result)