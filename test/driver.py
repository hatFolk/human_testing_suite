"""A Testing Module that makes random multiple choice questions from a text file."""
import math
import itertools
class Tests:
    dict = {}
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
    return {text[i].rstrip('\n'):eval(text[i+1].rstrip('\n')) for i in range(0, len(text), 2)}

def makeTest(list):
    text = []
    for i in list:
        if i[0] == '[':
            

def main(): #Run driver
    filename = open("multiple_choice.txt")
    text = filename.readlines()
    print(makeSuite(text))

if __name__ == "__main__": main()
