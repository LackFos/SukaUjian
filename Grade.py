from Database.Connect import Connect

class Grade:
    def __init__(self):
        self.__db = Connect()

    def insert(self, table, data):
        self.__db.insert(table, data)

    def delete(self, table, where):
        self.__db.delete(table, where)


nilai = Grade()