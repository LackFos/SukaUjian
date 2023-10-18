from Database.Connect import Connect

# test.execute_with_commit("INSERT INTO pbo VALUES('1', 'Wilsen', 'Test')")
# user = test.execute_select("SELECT Name FROM pbo")
# a = user[1]
# print(a)

# test = Conn()
# test.execute_with_commit("DELETE FROM pbo WHERE ID='1'")
# user = test.execute_select("SELECT * FROM pbo")
# print(user)
Conn = Connect()


class Auth():
    def __init__(self, user, passw):
        self.user = user
        self.__passw = passw

    def login(self):
        user = Conn.first("pbo", {"Name": a})
        passw = Conn.first("pbo", {"Password": b})
        if user and passw is not None:
            print("Login Succses")
            Auth.logout(main)
        else:
            print("Login Fail")

    def logout(self):
        print("Apakah %s Mau Keluar?" % self.user)
        keluar = input("1. Yes\n2. No\n")
        if keluar == "1":
            self.user = ""
            self.__passw = ""
            print("Berhasil Logout")
        else:
            print("Silahkan melanjutkan")


main = input(
    "What do you wanat to do\n1. Login\n2.Register\n3.Forget Password\n")

match main:
    case "1":
        a = input("Masukan Username\n")
        b = input("Masukan Password\n")
        main = Auth(a, b)
        Auth.login(main)
    case "2":
        a = input("Masukan Username Baru\n")
        b = input("Masukan Password Baru\n")
        Conn.insert("pbo", {"ID": None, "Name": a, "Password": b})
    case "3":
        pert = input("Masukan Username\n")
        pert2 = input("Masukan Password Baru\n")
        Conn.update("pbo", {"Name": pert}, {"Password": pert2})


#     # Conn.delete("user", {"Name": a})

#     print("done")
