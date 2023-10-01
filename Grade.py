from Database.Connect import Connect

class Grade:
    def __init__(self):
        self.__db = Connect()

    def insert(self, table, data):
        self.__db.insert(table, data)


nilai = Grade()