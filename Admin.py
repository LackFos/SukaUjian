from Database.Connect import Connect
import tkinter as tk


class Auth():
    def __init__(self, user, passw, npm):
        self.__user = user
        self.__passw = passw
        self.__npm = None
        self.Conn = Connect()

    def login(self):
        user = self.Conn.first("Admin", {"Name": self.__user})
        passw = self.Conn.first("Admin", {"Password": self.__passw})
        if user and passw is not None:
            print("Login Succses")
            return True
        else:
            print("Login Fail")

    def InputMahasiswaBaru(self, a, b, d):
        self.__user = a
        self.__passw = b
        self.__npm = d
        self.Conn.insert("Admin", {"Name": self.__user, "Password": self.__passw,
                                   "NPM": self.__npm, "Status": "Mahasiswa"})

    def InputDosenBaru(self, a, b, d, matakuliah):
        self.__user = a
        self.__passw = b
        self.__npm = d
        self.Conn.insert("Admin", {"Name": self.__user,
                                   "Password": self.__passw, "NPM": self.__npm, "Status": "Dosen", "Matakuliah": matakuliah})

    def DeleteUser(self, npm):
        self.Conn.delete("Admin", {"NPM": npm})

    def Updateuser(self, npm, passw):
        self.Conn.update("Admin", {"NPM": npm}, {"Password": passw})

    def Selectdata(self):
        a = self.Conn.select("exam", [])
        b = self.Conn.select("jadwal", [])
        for i in a:
            print(i)
        for i in b:
            print(i)


a, b, c = ["WilsenAdmin", "Test123", "1"]
main = Auth(a, b, c)
while (main):
    a = input(
        "Silahkan Pilih Aksi\n1. Input Mahasiswa Baru\n2. Input Dosen Baru\n3. Delete Mahasiswa/Dosen Lama\n4. Update Data Mahasiswa/Dosen\n5. Select Token, Jadwal, Dll\n6. Quit\n")
    match a:
        case "1":
            loop = True
            while (loop):
                a = input("Masukan Username\n")
                b = input("Masukan Password\n")
                d = input("Masukan NPM\n")
                main.InputMahasiswaBaru(a, b, d)
                d = input(
                    "Apakah ingin memasukan mahasiswa lain?\n1.Yes\n2.No\n")
                if d == "2":
                    break

        case "2":
            loop = True
            while (loop):
                a = input("Masukan Username\n")
                b = input("Masukan Password\n")
                e = input("Masukan NPD\n")
                d = input("Masukan Matakuliah\n")
                main.InputDosenBaru(a, b, e, d)
                d = input(
                    "Apakah ingin memasukan dosen lain?\n1.Yes\n2.No\n")
                if d == "2":
                    break
        case "3":
            loop = True
            while (loop):
                npm = input(
                    "Masukan npm mahasiswa/dosen yang ingin didelete\n")
                main.DeleteUser(npm)
                d = input(
                    "Apakah ingin mendelete mahasiswa lain?\n1.Yes\n2.No\n")
                if d == "2":
                    break
        case "4":
            loop = True
            while (loop):
                npm = input(
                    "Masukan npm mahasiswa/dosen yang ingin diu update\n")
                passw = input("Masukan password baru\n")
                main.Updateuser(npm, passw)
                d = input("Apakah ingin mengupdate data lain?\n1. Yes\n2. No\n")
                if d == "2":
                    break
        case "5":
            main.Selectdata()
            break
        case "6":
            print("Thank You")
            break
