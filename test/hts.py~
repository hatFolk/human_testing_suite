"""A Testing Module that makes random multiple choice questions from a text file."""
import sys
import random
# Such OOP. Very wow.
class Tests:
    database = {}
    numQuestions = 0
    def __init__(self, filename):
        file = open(filename, "rU")
        qlist = file.read() # Consider redoing this in readline()
        qlist = Tests.makeTest(self, qlist)
        for i in range(len(qlist)):
            print("{} : {}".format(i, qlist[i]))
        file.close()
        
    def makeSuite(self, text):
        """Takes a list of strings and creates a database of Question objects from it. Assumes that the first
        element of the multiple choice is the answer.
        Precondition: That the list is properly formatted."""
        i = 0
        while i < len(text):
            self.database[self.numQuestions] = Question(text[i].rstrip(), text[i+1])
            self.numQuestions += 1 
            i += 2
        
    def makeTest(self, text): # Fix the logic. Make simpler?
        qlist = text.split('\n\n\n')
        qlist = [k.split('***') for k in qlist]
        qlist = map(lambda y : filter(lambda x : x != '', y), qlist)
        
        return qlist
            
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
    def __iter__(self):
        x = list(range(self.numQuestions))
        for i in random.shuffle(x):
            yield self.database[i].askQuestion()
            
    def __len__(self):
        return self.numQuestions

    def __str__(self):
        str = ""
        for k, v in self.database.items():
            str += "Question {}:\n{}".format(k, v)
        return str

class Question:
    """Question object assumes that the first multiple choice answer is the correct answer """
    question = ""
    choice = []
    ans = ""
    def __init__(self, question, choice): # Assumes the answer is the first value of choice
        self.question = question
        self.choice = choice
        self.ans = choice[0]
    def getQuestion(self):
        return question
    def getChoice(self): # Randomizes choices and assigns a numerical for each.
        return {k+1:v for k, v in enumerate(random.shuffle(choice))}
    def getAnswer(self):
        return ans
    def askQuestion(self):
        print(getQuestion(self))
        multChoice = getChoice(self)
        for i in list(multChoice.keys()).sort():
            print("{}.\n{}".format(i, multChoice[i]))
    def __str__(self):
        return "Question:\n\t{}\nChoices:\n\t{}\nAnswer\n\t{}".format(self.question, self.choice, self.ans)

def main(filenames):
    """If filenames are passed in, they will be created as tests and then tested one by one"""
    if(filenames):
        for i in filenames:
            try:
                newTest = Tests(i)
                print(newTest)
                #newTest.startQuestions()
            except (FileNotFoundError, IndexError) as e:
                print("Problem! You got this : {}".format(e))

if __name__ == "__main__" : main(sys.argv[1:]) # element 0 only interesting if you want the name of your file...
