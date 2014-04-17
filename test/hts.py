"""A Testing Module that makes random multiple choice questions from a text file."""
import sys
import random
# Such OOP. Very wow.
class Tests:
    database = {}
    numQuestions = 0
    def __init__(self, filename):
        file = open(filename, "rU")
        qlist = file.read()
        qlist = self.makeTest(qlist)
        self.makeSuite(qlist)
        file.close()
        
    def makeSuite(self, text):
        """Takes a list of strings and creates a database of Question objects from it. Assumes that the first
        element of the multiple choice is the answer.
        Precondition: That the list is properly formatted."""
        i = 0
        while i < len(text):
            self.database[self.numQuestions] = Question(text[i][0], text[i+1])
            self.numQuestions += 1 
            i += 2
            
    def makeTest(self, text):
        text = text.split('\n\n\n')
        text = [i.split('***') for i in text if i[0]]
        i = 0
        while i < len(text):
            j = 0
            while j < len(text[i]): # You could probably do this with a combination of filter and map...
                if text[i][j] == '':
                    del text[i][j]
                else:
                    text[i][j] = text[i][j].rstrip()
                    j+=1
            i += 1
        return text
    
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
        except (KeyError, ValueError): # Exception handling...
                print("Invalid answer...")

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
    choice = {}
    ans = ""
    def __init__(self, question, choice): # Assumes the answer is the first value of choice
        random.seed()
        self.question = question
        self.ans = choice[0]
        self.choice = self.getChoice(choice)
        print(self.choice)
    def getQuestion(self):
        return question
    def getChoice(self, mult): # Randomizes choices and assigns a numerical for each.
        print(mult)
        random.shuffle(mult)
        return {k[0]:k[1] for k in enumerate(mult, 1)}
    
    def getAnswer(self):
        return ans
    def askQuestion(self):
        print(getQuestion(self))
        multChoice = getChoice(self)
        for i in list(multChoice.keys()).sort():
            print("{}.\n{}".format(i, multChoice[i]))
    def __str__(self):
        quest = ""
        quest += "Question : {}\n".format(self.question)
        for i in sorted(self.choice):
            if self.choice[i] == self.ans:
                quest += "***"
            quest += "{:0}\t:{:1}\n".format(i)
        return quest

def storeToFile(filename, test):
    file = open(test, "w+")
    data = list(test.getDatabase.values()) # Makes a list of all the question objects stored
    for i in data.values():
        return

def startTest(test):

def main(filenames):
    """If filenames are passed in, they will be created as tests and then tested one by one"""
    if(filenames):
        for i in filenames:
            try:
                newTest = Tests(i)
                #newTest.startQuestions()
            except (FileNotFoundError, IndexError) as e:
                

if __name__ == "__main__" : main(sys.argv[1:]) # element 0 only interesting if you want the name of your file...
