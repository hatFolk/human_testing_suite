"""A Testing Module that makes random multiple choice questions from a text file."""
import sys

class Tests:
    dict = {}
    x = 0
    def __init__(self):
        pass
    def start_test(self):
        pass
    def getdict(self):
        return dict
    def run(self):
        pass

def getRand():
    pass

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

def askQuestion(list, answer):
    print(list[0])
    choice = {num:choice for num, choice in enumerate(list[1], 1)}

def main(args): #Run driver
    filename = open("multiple_choice.txt", "rU")
    text = filename.readlines()
    makeTest(text)
    dict = makeSuite(text)
    print(dict)
    
if __name__ == "__main__": main(sys.argv)
