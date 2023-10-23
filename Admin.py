from Database.Connect import Connect

Conn = Connect()


class Auth():
    def __init__(self, user, passw):
        self.user = user
        self.passw = passw

    def login(self):
        user = Conn.first("pbo", {"Name": a})
        passw = Conn.first("pbo", {"Password": b})
        if user and passw is not None:
            print("Login Succses")
            return True
        else:
            print("Login Fail")

    def InputMahasiswaBaru(self):
        Conn.insert("pbo", {"ID": None, "Name": self.user,
                    "Password": self.passw})

    def DeleteMahasiswaLama(nama):
        Conn.delete("pbo", {"Name": nama})

    def UpdateMahasiswa(name, passw):
        Conn.update("pbo", {"Name": name}, {"Password": passw})


a, b = ["Wilsen", "Test123"]
main = Auth(a, b)
main.login()

while (main.login):
    a = input(
        "Silahkan Pilih Aksi\n1. Input Mahasiswa Baru\n2. Delete Mahasiswa Lama\n3. Update update mahasiswa\n4. Quit\n")
    match a:
        case "1":
            loop = True
            while (loop):
                a = input("Masukan Username\n")
                b = input("Masukan Password\n")
                c = Auth(a, b)
                c.InputMahasiswaBaru()
                d = input(
                    "Apakah ingin memasukan mahasiswaw lain?\n1.Yes\n2.No\n")
                if d == "2":
                    break
        case "2":
            loop = True
            while (loop):
                a = input("Masukan nama mahasiswa yang ingin didelete\n")
                Auth.DeleteMahasiswaLama(a)
                d = input(
                    "Apakah ingin mendelete mahasiswaw lain?\n1.Yes\n2.No\n")
                if d == "2":
                    break
        case "3":
            loop = True
            while (loop):
                a = input("Masukan nama mahasiswa yang ingin diu update\n")
                b = input("Masukan password baru\n")
                Auth.UpdateMahasiswa(a, b)
                d = input(
                    "Apakah ingin mendelete mahasiswaw lain?\n1.Yes\n2.No\n")
                if d == "2":
                    break
        case "4":
            print("Thank You")
            break
