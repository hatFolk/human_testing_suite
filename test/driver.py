"""A Testing Module that makes random multiple choice questions from a text file."""
import math
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
    return {text[i][0]:eval(text[i][1]) for i in range(len(text))}

def makeTest(list, i = 0):
    while i+1 < len(list):
        if list[i+1][0] != '[' :
            list[i] += list.pop(i+1)
        else:
            i += 2
    return list

def askQuestion(list, answer):
    print(list[0])
    choice = {num:choice for num, choice in enumerate(list[1], 1)}

def main(): #Run driver
    filename = open("multiple_choice.txt")
    text = filename.readlines()
    makeTest(text) # Made it use the same list efficiency?
    print(text)

if __name__ == "__main__": main()
