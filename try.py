import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Izzul123", 
    database="sukaujian"
)

if db.is_connected():
    print("Berhasil terhubung ke database")

cursor = db.cursor()
sql = "SELECT * FROM kelas2"
cursor.execute(sql)

results = cursor.fetchall()

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

for data in results:
    nomor, capacity, occupied = data[1], data[2], data[3]
    kelas = Kelas(nomor, capacity, occupied)
    kelas_list.append(kelas)

for kelas in kelas_list:
    kelas.pinjamKelas(30)
    kelas.kembalikanKelas()
