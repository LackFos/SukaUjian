import os
from Database.Connect import Connect

os.system("cls")
CONN = Connect()
ANSWER = []

class Exam:
    def __init__(self, timeLimit, subject):
        self.question = []
        self._timeLimit = timeLimit
        self.__subject = subject

    def get_question(self):
        list_question = CONN.select("soal")
        for data in list_question:
            question = data["soal_ujian"]
            self.question.append(question)

    def showSubject(self):
        print(f"Subject's Test was {self.__subject}")

    def start_exam(self, name):
        print(f"{name}, You have {self._timeLimit} hour to do your exam!")
        x = 0
        for x in range(len(self.question)):
            print(f"\n{x+1}. {self.question[x]}")
            answer = input("Answer: ")
            ANSWER.append(answer)

    def submit_exam(self):
        finishExam = input("Finish exam? type 'y' to finish: ")
        print("Your final answer: ")
        for x in range(len(ANSWER)):
            print(f"{x+1}. {ANSWER[x]}")
        

    # for only professor accessed
class Prof(Exam):
    def score(self, name):
        for x in range(len(ANSWER)):
            print(f"{x+1}. {ANSWER[x]}")

        score = int(input("Input score: "))
        return f"{name}'s final score was {score}"
    
    def input_question(self):
        still_input = True
        while still_input:
            isYes = input("Input question? ").lower()
            if isYes == "y":
                isInputting = input("Input question: \n")
                CONN.insert("soal", {"soal_ujian": isInputting}) 
            else:
                still_input = False
                # Expansion Auto Increment

    def view_current_question(self):
        list_question = CONN.select("soal")
        for data in list_question:
            no = data["nomor"]
            question = data["soal_ujian"]
            print(f"{no}. {question}")

def running_program(name):
    print("-"*50)
    compsci.get_question()
    compsci.showSubject()
    compsci.start_exam(name)
    compsci.submit_exam()


name_saved = "Jeffrey"
compsci = Exam(1, "Introduction to Computer Science 😄")
while compsci:
    status = input("Student or Prof? ").lower()
    if status == "student":
        isReady = input("Ready start exam? type 'ready' to start! ")
        if isReady:
            running_program(name=name_saved)
        print("You have finished your exams! 💪")
        compsci = False

    elif status == "prof":
        # in this case keyword to access prof is TIMB
        validateProf = input("Validate if you're a prof: ").upper()
        if validateProf == "TIMB":
            prof = Prof(1, "Introduction to Computer Science 😄")
            isDoing = input("Choose: \n - Score\n - Input questions\n - View questions\n --> ").lower()
            if isDoing == "score":
                print(prof.score(name_saved))
            elif isDoing == "input questions":
                prof.input_question()
            else: 
                prof.view_current_question()
            compsci = False
    else:
        compsci = False













# Start exam
# x = 0
        # for x in range(len(self.question)):
        #     print(f"\n{x+1}. {self.question[x]}")
        #     answer = input("Answer: ")
        #     CONN.__execute(f'CREATE TABLE `{name}` (nomor int, jawaban varchar(1000))', 1)