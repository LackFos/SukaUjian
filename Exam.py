import os
os.system("cls")

class Exam:
    def __init__(self, name, timeLimit, subject):
        self.__name = name
        self.question = ["What's computer? Please describe it!", "What's components that include as Hardware and Software? Please give me 5 each!", "What do you know about operation system?"]
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
    def score(self):
        for x in range(len(self.answer)):
            print(f"- {self.answer[x]}")

        score = int(input("Input score: "))
        return f"{self.__name}'s final score was {score}"


compsci = Exam("Jeffrey", 1, "Introduction to Computer Science 😄")
while compsci:
    isReady = input("Ready start exam? type 'ready' to start! ")

    if isReady:
        print("------------------------------------------------------------")
        compsci.showSubject()
        compsci.start_exam()
        compsci.submit_exam()
    break
print("You have finished your exams! Score will be announced in 3days. Goodluck!💪")
    
print("Fill anything you want!")
isProffesors = input("\nInput the message: ")
if isProffesors == "TIMB":
    print(compsci.score())
