class Auth():
    def __init__(self, user, passw):
        self.user = user
        self._passw = passw
        self.__successlogin = False

    def login(self):
        username = "test"
        password = "test123"
        if self.user == username and self._passw == password:
            print("login berhasil")
            self.__successlogin = True
        else:
            print("Login Gagal")

    def logout(self):
        if self.__successlogin == True:
            print("Apakah %s Mau Keluar?" % self.user)
            keluar = input("1. Yes\n2. No\n")
            if keluar == "1":
                self.user = ""
                self._passw = ""
                print("Berhasil Logout")
            else:
                print("Silahkan melanjutkan")
        else:
            return 0


a = input("Username: ")
b = input("Password: ")

main = Auth(a, b)

Auth.login(main)
Auth.logout(main)

print(f"{main.user}")
print(f"{main._passw}")
print(f"{main.__successlogin}")
