import os
from Database.Connect import Connect

os.system("cls")
CONN = Connect()

class Exam:
    def __init__(self, timeLimit, subject):
        self.question = []
        self._timeLimit = timeLimit
        self.__subject = subject
        self.answer = []

    def showSubject(self):
        print(f"Subject's Test was {self.__subject}")

    def start_exam(self):
        print(f"You have {self._timeLimit} hour to do your exam!")
        x = 0
        for x in range(len(self.question)):
            print(f"\n{x+1}. {self.question[x]}")
            answer = input("Answer: ")
            self.answer.append(answer)

    def submit_exam(self):
        finishExam = input("Finish exam? type 'y' to finish: ")

    # for only professor accessed
class Dosen(Exam):
    def __init__(self, name):
        super().__init__("", "")
        self.__name = name

    def score(self):
        for x in range(len(self.answer)):
            print(f"- {self.answer[x]}")

        score = int(input("Input score: "))
        return f"{self.__name}'s final score was {score}"
    
    def input_question(self):
        validation = input("Wanna input questions? ")

        if validation:
            isInputting = input("Input question: \n")
            CONN.insert("soal", {"soal_ujian": isInputting})



# dosen1 = Dosen("Jeffrey")
# dosen1.input_question()
CONN.select("soal")

# compsci = Exam("Jeffrey", 1, "Introduction to Computer Science 😄")
# while compsci:
#     isReady = input("Ready start exam? type 'ready' to start! ")

#     if isReady:
#         print("------------------------------------------------------------")
#         compsci.showSubject()
#         compsci.start_exam()
#         compsci.submit_exam()
#     break
# print("You have finished your exams! Score will be announced in 3days. Goodluck!💪")
    
# print("Fill anything you want!")
# isProffesors = input("\nInput the message: ")
# if isProffesors == "TIMB":
#     print(compsci.score())
