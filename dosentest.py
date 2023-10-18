import mysql.connector
from Database.Connect import Connect

class Dosen:
    def __init__(self,id):
        self.db=Connect()
        Result=self.db.first('dosen',{"ID":id})
        self.id=Result["ID"]

dosen1=Dosen(1)
print(dosen1.id)