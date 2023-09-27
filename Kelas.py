class Kelas:
    def __init__(self, nomor, capacity, occupied):
        self.__nomor = nomor
        self.__capacity = capacity
        self.__occupied = occupied

    def pinjamKelas(self, banyakMahasiswa):
        if(self.__occupied):
            print("Kelas", self.__nomor ,"ini sudah dipakai")
            return 
        
        if(banyakMahasiswa > self.__capacity):
            print("Kelas", self.__nomor ,"ini tidak muat")
        else:
            print("Kelas", self.__nomor ,"ini berhasil dipinjam")
            self.occupied = True

    def kembalikanKelas(self):
        self.occupied = False

kelas_315 = Kelas("315", 30, False)
kelas_315.pinjamKelas(39)

