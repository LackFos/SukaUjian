from Database.Connect import Connect

class Grade:
    def __init__(self):
        self.__db = Connect()

    def insert(self, table, data):
        self.__db.insert(table, data)

    def delete(self, table, where):
        self.__db.delete(table, where)

    def calculateGrade(self, score):
        if score >= 80:
            return "A"
        elif score >= 60:
            return "B"
        elif score >= 40:
            return "C"
        elif score >= 20:
            return "D"
        else:
            return "E"



nilai = Grade()