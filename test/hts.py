"""A Testing Module that makes random multiple choice questions from a text file."""
import sys
import random
# Such OOP. Very wow.
class Tests:
    database = {}
    numQuestions = 0
    def __init__(self, filename):
        """Tests is initialized with a filename containing Questions. This builds the database to test from"""
        file = open(filename, "rU")
        qlist = Tests.makeTest(self, file.readlines())
        for i in range(len(qlist)):
            print("{} : {}".format(i, qlist[i]))
        self.database = Tests.makeSuite(self, qlist)
        print(self.database)
    
    def makeSuite(self, text):
        i = 0
        while i < len(text):
            print(i)
            print(text[i].rstrip())
            print(eval(text[i+1]))
            print(eval(text[i+1])[int(text[i+2])])
            self.database[self.numQuestions] = Question(text[i].rstrip(), eval(text[i+1]), eval(text[i+1])[int(text[i+2])])
            self.numQuestions += 1
            i += 3

    def makeTest(self, xs): # Fix the logic. Make simpler?
        i = 0
        while i < len(xs)-1:
            if xs[i+1] == '\n':
                xs.pop(i+1)
                i += 1
            elif xs[i+1][0] == '[':
                if xs[i+1][-2] == ']':
                    i += 2
                else:
                    i += 1
                    while xs[i+1]=='\n' or xs[i+1][-2] != ']':
                        xs[i] += xs.pop(i+1)
            else:
                xs[i] += xs.pop(i+1)
        return xs

    def getDatabase(self):
        return self.database

    def askQuestion(question, list):
        choice = {k:v for k, v in enumerate(list[0])}
        print(question)
        for i in choice.items().sort():
            print("\t{}. {}".format(i[0], i[1]))
        ans = input("[Pick your number] > ")
        try:
            print("Correct!" if list[1] == choice[int(ans)] else "Wrong..., the answer was : {}".format(list[1]))
            return list[1] == choice[int(ans)]
        except (KeyError, ValueError):
                print("Invalid answer...")

    def startQuestions(self, x = numQuestions):
        points = 0
        ctr = 0
        questions = list(self.database.keys())[:x]
        random.shuffle(questions)
        print(questions)
        while questions: #i.e., questions still have things in it
            if tests.askQuestion(questions[ctr], self.database[questions[ctr]]):
                points += 1
            choice = input("\t[Remove Question? Type 'Yes' or 'yes', else it will be kept] > ")
            if choice.lower() == 'yes':
                questions.pop(ctr)        
        print("points = {}; x = {} ;".format(points, x)) 
        print("That's all the questions! Your Percent Accuracy: {}".format(points/x))

    def __len__(self):
        return self.numQuestions

    def __str__(self):
        str = ""
        for k, v in self.dict.items():
            str += "Question:\n{}\n\tChoices:\n\t{}\n\tAnswer: {}\n".format(k, v[0], v[1])
        return str

class Question:
    question = ""
    choice = []
    ans = ""
    def __init__(self, question, choice, ans):
        self.question = question
        self.choice = choice
        self.ans = ans
    def getQuestion(self):
        return question
    def getChoice(self):
        return enumerate(choice)
    def getAnswer(self):
        return ans
    def askQuestion(self):
        print(getQuestion(self))
        multChoice = getChoice(self)
        for i,j in multChoice:
            print("{}.\n{}".format(i, j))
    def __str__(self):
        return "Question:\n\t{}\nChoices:\n\t{}\nAnswer\n\t{}".format(self.question, self.choice, self.ans)

def main(filenames):
    """If filenames are passed in, they will be created as tests and then tested one by one"""
    if(filenames):
        for i in filenames:
            try:
                newTest = Tests(i)
                #newTest.startQuestions()
            except (FileNotFoundError, IndexError) as e:
                print("Problem! You got this : {}".format(e))
    else:
        # Interactive mode
        print("Development...")

if __name__ == "__main__" : main(sys.argv[1:]) # element 0 only interesting if you want the name of your file...
