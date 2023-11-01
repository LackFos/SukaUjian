from Database.Connect import Connect


class Auth():
    def __init__(self):
        self.__user = None
        self.__passw = None
        self.__npm = None
        self.Conn = Connect()

        while (True):
            a = input(
                "Silahkan Pilih Aksi\n1. Input Mahasiswa Baru\n2. Input Dosen Baru\n3. Delete Mahasiswa/Dosen Lama\n4. Update Data Mahasiswa/Dosen\n5. Select Token, Jadwal, Dll\n6. Quit\n")
            match a:
                case "1":
                    loop = True
                    while (loop):
                        a = input("Masukan Username\n")
                        b = input("Masukan Password\n")
                        d = input("Masukan NPM\n")
                        self.InputMahasiswaBaru(a, b, d)
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
                        self.InputDosenBaru(d)
                        d = input(
                            "Apakah ingin memasukan dosen lain?\n1.Yes\n2.No\n")
                        if d == "2":
                            break
                case "3":
                    loop = True
                    while (loop):
                        npm = input(
                            "Masukan npm mahasiswa/dosen yang ingin didelete\n")
                        self.DeleteUser(npm)
                        d = input(
                            "Apakah ingin mendelete mahasiswa lain?\n1.Yes\n2.No\n")
                        if d == "2":
                            break
                case "4":
                    loop = True
                    while (loop):
                        a = input(
                            "Masukan npm mahasiswa/dosen yang ingin diu update\n")
                        b = input("Masukan password baru\n")
                        self.Updateuser(a, b)
                        d = input(
                            "Apakah ingin mendelete mahasiswa lain?\n1.Yes\n2.No\n")
                        if d == "2":
                            break
                case "5":
                    self.Selectdata()
                    break
                case "6":
                    print("Thank You")
                    break

    def login(self):
        user = self.Conn.first("Admin", {"Name": self.__user})
        passw = self.Conn.first("Admin", {"Password": self.__passw})
        if user and passw is not None:
            print("Login Succses")
            return True
        else:
            print("Login Fail")

    def InputMahasiswaBaru(self):
        self.Conn.insert("Admin", {"Name": self.__user, "Password": self.__passw,
                                   "NPM": self.__npm, "Status": "Mahasiswa"})

    def InputDosenBaru(self, matakuliah):
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


# a, b, c = ["WilsenAdmin", "Test123", "1"]
main = Auth()
# Push Ulang
