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
    def login(self):
        user = Conn.first("pbo", {"Name": a})
        passw = Conn.first("pbo", {"Password": b})
        print(user, passw)

    def logout(self):
        if self.__successlogin == True:
            print("Apakah %s Mau Keluar?" % self.user)
            keluar = input("1. Yes\n2. No\n")
            if keluar == "1":
                self.user = ""
                self.__passw = ""
                print("Berhasil Logout")
            else:
                print("Silahkan melanjutkan")
        else:
            return 0


main = input("Do you want to login / register?\n1. Login\n2.Register")

if main == '1':
    a = input("Masukan Username\n")
    b = input("Masukan Password\n")
    main = Auth()
    Auth.login(main)
    # Auth.logout(main)
else:
    a = input("Masukan Username Baru\n")
    b = input("Masukan Password Baru\n")
    # Conn.insert("user", {"Name": a, "Password": b})
    # Conn.update("user", {"Name": a}, {"Password": b})
    # Conn.delete("user", {"Name": a})

    print("done")
