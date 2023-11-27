import os
import random
from Database.Connect import Connect

os.system("cls")

class Exam:
    def __init__(self):
        self.mydb = Connect()

        # Code dibawah ini belum diperlukan untuk mengerjakan tugas ini
        # if self.isAdmin:
        #     print("1. Insert session\n2. Update session\n3. Delete session")
        #     isInput = int(input("Which method? fill number: "))
        #     if isInput == 1:
        #         self.session_token()
        #         self.insert_session()
        #     elif isInput == 2: 
        #         self.update_session()
        #     elif isInput == 3:
        #         self.delete_session()
                
        # elif self.isAdmin == False:
        #     self.get_session = self.mydb.select("exam")
        #     for data in self.get_session:
        #         id = data["id"]
        #         sess = data["session"]
        #         print(f"{id}. {sess}")

        #     user_input = int(input("Input which session to do: "))
        #     input_token = input("Input token to access the questions: ")
        #     self.validate_token(input_token, user_input=user_input)
                
    def validate_token(self, token, user_input):
        indicator_id = self.mydb.first("exam", {"id": user_input}, ["token"])
        if token == indicator_id["token"]:
            print("You have accessed to the question")
        else:
            print("You failed to access the questions")

    def session_token(self):
        self.session = input("Input session: ")
        self.token = ""
        for _ in range(5):
            tokenn = str(random.randint(0,9))
            self.token += tokenn

    def insert_session(self):
        self.mydb.insert("exam", {"session": self.session, "token": self.token})

    def update_session(self):
        print(self.mydb.select("exam", ["id", "session", "token"]))
        self.whichUpdated = input("which id want to be updated? ")
        self.session_token()
        self.mydb.update("exam", {"id": self.whichUpdated}, {"session": self.session, "token": self.token})
            
    def delete_session(self):
        print(self.mydb.select("exam", ["id", "session", "token"]))
        deleteSession = input("which id to delete? ")
        self.mydb.delete("exam", {"id": deleteSession})


class Programming(Exam):
    def __init__(self, mataKuliah):
        super().__init__()
        self.mataKuliah = mataKuliah

    def view_token(self):
        get_token = self.mydb.first("exam", {"session": self.mataKuliah})
        return get_token["token"]
    
Programming_session = Programming("Session Programming")
print(f"Token untuk {Programming_session.mataKuliah} adalah {Programming_session.view_token()}")