from Database.Connect import Connect
Conn = Connect()


class Auth():
    def __init__(self, user, passw, npm):
        self.__user = user
        self.__passw = passw
        self.__npm = npm

    def login(self):
        user = Conn.first("Admin", {"Name": a})
        passw = Conn.first("Admin", {"Password": b})
        if user and passw is not None:
            print("Login Succses")
            return True
        else:
            print("Login Fail")

    def InputMahasiswaBaru(self):
        Conn.insert("Admin", {"Name": self.__user,
                              "Password": self.__passw, "NPM": self.__npm, "Status": "Mahasiswa"})

    def InputDosenBaru(self, matakuliah):
        Conn.insert("Admin", {"Name": self.__user,
                              "Password": self.__passw, "NPM": self.__npm, "Status": "Dosen", "Matakuliah": matakuliah})

    def DeleteUser(npm):
        Conn.delete("Admin", {"NPM": npm})

    def UpdateMahasiswa(npm, passw):
        Conn.update("Admin", {"NPM": npm}, {"Password": passw})

    def Selectdata(self):
        Conn.select("admin", "exam")
        Conn.select("admin", "jadwal")


a, b, c = ["WilsenAdmin", "Test123", "1"]
main = Auth(a, b, c)
main.login()

while (main.login()):
    a = input(
        "Silahkan Pilih Aksi\n1. Input Mahasiswa Baru\n2. Input Dosen Baru\n3. Delete Mahasiswa/Dosen Lama\n4. Update Data Mahasiswa/Dosen\n5. Select Token, Jadwal, Dll\n6. Quit\n")
    match a:
        case "1":
            loop = True
            while (loop):
                a = input("Masukan Username\n")
                b = input("Masukan Password\n")
                d = input("Masukan NPM\n")
                c = Auth(a, b, d)
                c.InputMahasiswaBaru()
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
                c = Auth(a, b, e)
                c.InputDosenBaru(d)
                d = input(
                    "Apakah ingin memasukan dosen lain?\n1.Yes\n2.No\n")
                if d == "2":
                    break
        case "3":
            loop = True
            while (loop):
                npm = input(
                    "Masukan npm mahasiswa/dosen yang ingin didelete\n")
                Auth.DeleteUser(npm)
                d = input(
                    "Apakah ingin mendelete mahasiswa lain?\n1.Yes\n2.No\n")
                if d == "2":
                    break
        case "4":
            loop = True
            while (loop):
                a = input("Masukan npm mahasiswa/dosen yang ingin diu update\n")
                b = input("Masukan password baru\n")
                Auth.UpdateMahasiswa(a, b)
                d = input(
                    "Apakah ingin mendelete mahasiswa lain?\n1.Yes\n2.No\n")
                if d == "2":
                    break
        case "5":
            a.Selectdata()
            break
        case "6":
            print("Thank You")
            break
