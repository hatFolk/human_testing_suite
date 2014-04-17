"""A Testing Module that makes random multiple choice questions from a text file."""
import sys
import random
# Such OOP. Very wow.
class Test:
    """Takes w """
    database = {}
    numQuestions = 0
    def __init__(self, filename):
        file = open(filename, "rU")
        qlist = file.read()
        qlist = self.makeTest(qlist)
        self.makeSuite(qlist)
        file.close()
        
    def makeSuite(self, text):
        i = 0
        while i < len(text):
            self.database[self.numQuestions] = Question(text[i][0], text[i+1])
            self.numQuestions+=1
            i+=2

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

    def __iter__(self):
        x = list(range(self.numQuestions))
        random.shuffle(x)
        for i in x:
            yield self.database[i]
            
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
        self.choice = self.generateChoices(choice)

    def generateChoices(self, mult):
        """Shuffles a list and puts it in a dictionary as a value.
        The key starts at 1 and ends at the length of the list"""
        random.shuffle(mult)
        return {k[0]:k[1] for k in enumerate(mult, 1)}
    
    def askQuestion(self):
        """Asks the question. Gets an answer.
        Returns False if answered correctly. Returns True."""
        print(self.question)
        multChoice = getChoice(self)
        for i in sorted(multChoice):
            print("{}.\n{}".format(i, multChoice[i]))
        num = input("[Which number is the answer?] > ")
        try:
            return not (self.choice[int(num)] == self.ans)
        except:
            return True
            
    def __str__(self):
        quest = ""
        quest += "{}\n\n".format(self.question)
        for i in sorted(self.choice):
            if self.choice[i] == self.ans:
                quest += "***"
            quest += "Choice {}.\n\n{}\n\n".format(i, self.choice[i])
        return quest

def main(filenames):
    """If filenames are passed in, they will be created as tests and then tested one by one"""
    if(filenames):
        for i in filenames:
            newTest = Test(i) #Make a Test object
            answeredWrong = []
            for j in newTest:
                if j.askQuestion():
                    answeredWrong.append(j)
            print("Please review these questions!")
            for k in answeredWrong:
                print(k.question)

if __name__ == "__main__" : main(sys.argv[1:]) # element 0 only interesting if you want the name of your file...
