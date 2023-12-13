from test3 import MyDB

conn = MyDB()
conn_db, cursor_db = conn.connect()

class Mahasiswa:
    def __init__(self, conn, cursor, npm, nama, matakuliah, jumlahsks):
        self.conn = conn
        self.cursor = cursor
        self.__nama = nama
        self.__npm = npm
        self.matakuliah = matakuliah
        self._jumlahsks = jumlahsks

    def enroll_kelas(self):
        return f"{self.__nama} dengan npm {self.__npm} sedang enroll matakuliah {self.matakuliah} dengan jumlah sks {self._jumlahsks}"

    def take_exam(self):
        return f"{self.__nama} dengan npm {self.__npm} mengambil ujian {self.matakuliah}"
    
    def select_mahasiswa(self):
        query = f"SELECT * FROM Mahasiswa WHERE npm = {self.__npm}"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result:
            return f"Mahasiswa {self.__nama} dengan npm {self.__npm} ditemukan dengan data: {result}"
        else:
            return f"Mahasiswa {self.__nama} dengan npm {self.__npm} tidak ditemukan."

    def insert_mahasiswa(self):
        query = f"INSERT INTO Mahasiswa (nama, npm, matakuliah, jumlahsks) VALUES ('{self.__nama}', {self.__npm}, '{self.matakuliah}', {self._jumlahsks})"
        self.cursor.execute(query)
        self.conn.commit()

    def update_mahasiswa(self, jumlahsks):
        query = f"UPDATE Mahasiswa SET jumlahsks = {jumlahsks} WHERE nama = '{self.__nama}'"
        self.cursor.execute(query)
        self.conn.commit()


    def delete_mahasiswa(self):
        query = f"DELETE FROM Mahasiswa WHERE nama = '{self.__nama}'"
        self.cursor.execute(query)
        self.conn.commit()

mahasiswa1 = Mahasiswa(conn=conn_db, cursor=cursor_db, npm=2232025, nama="kevin", matakuliah="Mandarin", jumlahsks=2)

print(mahasiswa1.enroll_kelas())
print(mahasiswa1.take_exam())

result = mahasiswa1.select_mahasiswa()
print(result)


# mahasiswa1.insert_mahasiswa()
# mahasiswa1.update_mahasiswa(jumlahsks=1)
# mahasiswa1.delete_mahasiswa()
