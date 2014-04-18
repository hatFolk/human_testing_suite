"""A Testing Module that makes random multiple choice questions from a text file."""
import sys
import random
# Such OOP. Very wow.
class Test:
    """Takes a file, breaks it up into Question and
    Multiple Choices and make Question objects"""
    database = {}
    numQuestions = 0
    def __init__(self, filename):
        """Constructor for Tests.
        Takes a file and parses it for Questions"""
        file = open(filename, "rU")
        qlist = file.read()
        qlist = self.makeTest(qlist)
        self.makeSuite(qlist)
        file.close()
        
    def makeTest(self, text):
        """Take a block of text from a file and makes it usable for makeSuite."""
        text = text.split('\n\n\n')
        text = [i.split('***') for i in text]
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

    def makeSuite(self, text):
        """Takes a parsed text list and puts it into a Question object database.
        Precondition: text has already been through makeTest"""
        i = 0
        while i < len(text):
            self.database[self.numQuestions] = Question(text[i][0], text[i+1])
            self.numQuestions+=1
            i+=2
    
    def __iter__(self):
        """Makes Test iterable after shuffling the questions"""
        x = list(range(1, self.numQuestions))
        random.shuffle(x)
        for i in x:
            yield self.database[i]
        raise StopIteration

    def __len__(self):
        """The length of Tests should be the number of Questions...
        Which is numQuestions."""
        return self.numQuestions

    def __str__(self):
        """And if you print a Test, what does it look like?"""
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
        """Constructor for Questions."""
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
        for i in sorted(self.choice):
            print("{}.\n    {}".format(i, self.choice[i].replace('\n','\n    ')))
        print("")
        num = input("[Which number is the answer?] > ")
        print("")
        try:
            return not (self.choice[int(num)] == self.ans)
        except:
            return True
            
    def __str__(self):
        """Mainly for Debug and telling people that they did something wrong."""
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
            print("Please review these questions!:\n")
            i = 1
            for k in answeredWrong:
                print("{}.\n    {}\n".format(i, k.question.replace('\n', '\n    ')))
                i += 1

if __name__ == "__main__" : main(sys.argv[1:]) # element 0 only interesting if you want the name of your file...
