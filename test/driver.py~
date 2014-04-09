"""A Testing Module that makes random multiple choice questions from a text file."""
import sys

class tests:
    database = {}
    numQuestions = 0
    def __init__(self, filename):
        """Tests is initialized with a filename containing Questions. This builds the database to test from"""
        file = open(filename, "rU")
        self.database = tests.makeSuite(tests.makeTest(file.readlines()))
        self.numQuestions = len(self.dict.items())
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
    def __len__(self):
        return numQuestions
    def __str__(self):
        str = ""
        for k, v in self.dict.items():
            str += "Question:\n{}\n\tChoices:\n\t{}\n\tAnswer: {}\n".format(k, v[0], v[1])
        return str

def askQuestion(list):
    print(list[0])
    choice = {num:choice for num, choice in enumerate(list[1], 1)}

def main(args): #Run driver
    x = tests("multiple_choice.txt")
    print(x)
    
if __name__ == "__main__": main(sys.argv)
