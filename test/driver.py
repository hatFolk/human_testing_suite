"""A Testing Module that makes random multiple choice questions from a text file."""
import sys

class tests:
    dict = {}
    x = 0
    def __init__(self, filename):
        file = open(filename, "rU")
        self.dict = tests.makeSuite(tests.makeTest(file.readlines()))
        self.x = len(self.dict.items())
    def makeSuite(text):
        return {text[i].rstrip():[eval(text[i+1]), text[i+2].rstrip()] for i in range(0, len(text), 3)}
    def makeTest(list):
        i = 0
        while i < len(list)-1:
            if list[i+1] == '\n':
                list.pop(i+1)
                i += 1
            elif list[i+1][0] == '[':
                i += 2
            else:
                list[i] += list.pop(i+1)
        return list
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
