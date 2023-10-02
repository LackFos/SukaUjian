import os
from Database.Connect import Connect

os.system("cls")
CONN = Connect()

class Exam:
    def __init__(self, name, timeLimit, subject):
        self.__name = name
        self.question = []
        self._timeLimit = timeLimit
        self.__subject = subject
        self.answer = []

    def get_question(self):
        list_question = CONN.select("soal")
        for data in list_question:
            question = data["soal_ujian"]
            self.question.append(question)

    def showSubject(self):
        print(f"Subject's Test was {self.__subject}")

    def start_exam(self):
        print(f"{self.__name}, You have {self._timeLimit} hour to do your exam!")
        x = 0
        for x in range(len(self.question)):
            print(f"\n{x+1}. {self.question[x]}")
            answer = input("Answer: ")
            self.answer.append(answer)

    def submit_exam(self):
        finishExam = input("Finish exam? type 'y' to finish: ")

    # for only professor accessed
class Prof(Exam):
    def __init__(self, name, timelimit, subject):
        super().__init__(name, timelimit, subject)

    def score(self):
        for x in range(len(self.answer)):
            print(f"- {self.answer[x]}")

        score = int(input("Input score: "))
        return f"{self._Exam__name}'s final score was {score}"
    
    def input_question(self):
        still_input = False
        while not still_input:
            if input("Input question? "):
                isInputting = input("Input question: \n")
                CONN.insert("soal", {"soal_ujian": isInputting}) 
                # Expansion Auto Increment

    def view_current_question(self):
        list_question = CONN.select("soal")
        for data in list_question:
            no = data["nomor"]
            question = data["soal_ujian"]
            print(f"{no}. {question}")

compsci = Exam("Jeffrey", 1, "Introduction to Computer Science 😄")

while compsci:
    status = input("Student or Prof? ").lower()
    if status == "student":
        isReady = input("Ready start exam? type 'ready' to start! ")
        if isReady:
            print("------------------------------------------------------------")
            compsci.get_question()
            compsci.showSubject()
            compsci.start_exam()
            compsci.submit_exam()
        print("You have finished your exams! 💪")
        compsci = False

    elif status == "prof":
        # in this case keyword to access prof is TIMB
        validateProf = input("Validate if you're a prof: ").upper()
        if validateProf == "TIMB":
            prof = Prof("Jeffrey", 1, "Introduction to Computer Science 😄")
            isDoing = input("Choose: \n - Score\n - Input questions\n - View questions\n --> ").lower()
            if isDoing == "score":
                print(prof.score())
            elif isDoing == "input questions":
                prof.input_question()
            else: 
                prof.view_current_question()
        compsci = False
    
    else:
        compsci = False