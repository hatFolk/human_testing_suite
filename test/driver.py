"""A Testing Module that makes random multiple choice questions from a text file."""
import sys
import random

class tests:
    database = {}
    numQuestions = 0
    def __init__(self, filename):
        """Tests is initialized with a filename containing Questions. This builds the database to test from"""
        file = open(filename, "rU")
        self.database = tests.makeSuite(self, tests.makeTest(self, file.readlines()))
        self.numQuestions = len(self.database)
    
    def makeSuite(self, text):
        return {text[i].rstrip():[eval(text[i+1]), text[i+2].rstrip()] for i in range(0, len(text), 3)}

    def makeTest(self, xs):
        i = 0
        while i < len(xs)-1:
            if xs[i+1] == '\n':
                xs.pop(i+1)
                i += 1
            elif xs[i+1][0] == '[':
                i += 2
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
    def __str__(self):
        return "Hi"

def main(filenames):
    """If filenames are passed in, they will be created as tests and then tested one by one"""
    if(filenames):
        for i in filenames:
            try:
                test_n = tests(i)
                test_n.startQuestions()
            except (FileNotFoundError, IndexError) as e:
                print("Problem! You got this : {}".format(e))

if __name__ == "__main__" : main(sys.argv[1:]) # element 0 only interesting if you want the name of your file...
