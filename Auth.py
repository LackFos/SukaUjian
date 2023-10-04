import mysql.connector


class Conn():
    __mydb = None

    # constructor
    def __init__(self):
        self.__mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="wilsen",
        )

    def execute_with_commit(self, sql):
        cursor = self.__mydb.cursor()
        cursor.execute(sql)
        self.__mydb.commit()

    def execute_select(self, sql):
        cursor = self.__mydb.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


test = Conn()
# test.execute_with_commit("INSERT INTO pbo VALUES('1', 'Wilsen', 'Test')")
# user = test.execute_select("SELECT Name FROM pbo")
# a = user[1]
# print(a)

# test = Conn()
# test.execute_with_commit("DELETE FROM pbo WHERE ID='1'")
# user = test.execute_select("SELECT * FROM pbo")
# print(user)


class Auth():
    def __init__(self, user, passw):
        self.user = user
        self.__passw = passw
        self.__successlogin = False

    def login(self):
        user = test.execute_select("SELECT Name FROM pbo")
        a = user[0]
        passs = test.execute_select("SELECT Password FROM pbo")
        password = passs[0]
        if self.user == a[0] and self.__passw == password[0]:
            print("login berhasil")
            self.__successlogin = True
        else:
            print("Login Gagal")
        print(a)
        print(self.user)

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
    main = Auth(a, b)
    Auth.login(main)
    Auth.logout(main)
else:
    a = input("Masukan Username Baru\n")
    b = input("Masukan Password Baru\n")
    s = "INSERT INTO pbo VALUES('1', '%s', '%s')" % (a, b)
    test = Conn()
    test.execute_with_commit(s)
    print("done")
