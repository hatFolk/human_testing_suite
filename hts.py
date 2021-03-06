"""A Testing Module that makes random multiple choice questions from a text file."""
import sys
import random
# Such OOP. Very wow.

class Test:
    """Takes a file, breaks it up into Question and
    Multiple Choices and make Question objects"""
    def __init__(self, filename, rndQ=True, rndA=True):
        """Constructor for Tests.
        Takes a file and parses it for Questions"""
        self.database = {}
        self.numQuestions = 0
        self.rndQ = rndQ
        self.rndA = rndA
        file = open(filename, "rU")
        qlist = file.read()
        qlist = self.makeTest(qlist)
        self.makeSuite(qlist)
        file.close()
        
    def makeTest(self, text):
        """Take a block of text from a file and makes it usable for makeSuite."""
        text = text.split('\n\n\n') # Splits the large text file everytime there's 3 \n in a row
        text = [i.split('***') for i in text] #Splits each element with the multiple choice to be a list of lists
        # ^ That's probably going to be every other line. But I have it going through all of them.
        i = 0
        while i < len(text): # I wanted to modify the list above in place. Try and save a little memory...
            j = 0
            while j < len(text[i]): # You could probably do this with a combination of filter and map...
                if text[i][j] == '': # Had an issue with "random" '' elements
                    del text[i][j]
                else:
                    text[i][j] = text[i][j].rstrip() #Those pesky extra newlines
                    j+=1
            i += 1
        return text # Return the list

    def makeSuite(self, text):
        """Takes a parsed text list and puts it into a Question object database.
        Precondition: text has already been through makeTest
        AND text[i+1][0] is the CORRECT answer to the question"""
        for i in range(0, len(text), 2): #Build the database based off of what number its on.
            self.database[self.numQuestions] = Question(text[i][0], text[i+1], self.rndA) #i is the question, i+1 is the ans
            self.numQuestions+=1

    def __iter__(self):
        """Makes Test iterable after shuffling the questions.
        Assumes that the user wanted the questions randomly."""
        x = list(range(self.numQuestions))
        if self.rndQ : random.shuffle(x) # Is there a way to 'toggle' the randomness?
        for i in x:
            yield self.database[i]
        raise StopIteration #TIL: To make an __iter__ you should raise this

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

    def __repr__(self):
        return "Test Object @ {} with {} questions".format(id(self), self.numQuestions)

class Question:
    """Question object assumes that the first multiple choice answer is the correct answer """
    question = ""
    ans = ""
    def __init__(self, question, choice, rand=True): # Assumes the answer is the first value of choice
        """Constructor for Questions."""
        self.question = question
        self.ans = choice[0]
        self.choice = Choices(choice, rand)

    
    def askQuestion(self):
        """Asks the question. Gets an answer.
        Returns False if answered correctly. Returns True."""
        print(self.question) #Prints the question
        print(self.choice) #Prints the answers
        num = input("\n[Choice?] > ")
        print("")
        try:
            return (self.choice.choices[int(num)] == self.ans) #True if you picked the right answer #Prints the answers
        except:
            return False #False if you picked otherwise
            
    def __str__(self):
        """Mainly for Debug and telling people that they did something wrong."""
        return "{}\n\n".format(self.question)

    def __repr__(self):
        return "Question Object @ {}".format(id(self))

class Choices:
    """Makes a list of Choices"""
    def __init__(self, mult, rand=True):
        self.choices = self.makeChoices(mult, rand)

    def makeChoices(self, mult, rand=True):
        """Shuffles a list and puts it in a dictionary as a value.
        The key starts at 1 and ends at the length of the list"""
        if rand: random.shuffle(mult)
        return {k[0]:k[1] for k in enumerate(mult, 1)} 

    def __iter__(self):
        for i in self.choices.values():
            yield i
        raise StopIteration

    def __str__(self):
        s = ""
        for i in sorted(self.choices):
            s += "{}.\n    {}\n".format(i, self.choices[i].replace("\n", "\n    ")) # Makes a nicely formatted thing.
        return s

def exportTest(xs, filename):
    """xs is a list of questions. filename is where the tests will be stored"""
    test = open(filename, "w")
    x = ""
    for i in xs:
        x += "{}\n\n\n***{}\n".format(i.question, i.ans)
        for j in i.choice:
            if j != i.ans:
                x+="***{}\n".format(j)
        x += "\n\n"
    test.write(x[:-3])
    test.close()


def takeExam(filenames):
    """If filenames are passed in, they will be created as tests and then tested one by one
    Acts as main function when hts.py used as program, not module"""
    if(filenames):
        for i in filenames:
            newTest = Test(i) #Make a Test object
            print("{} Questions Created!".format(len(newTest)))
            ctr = int(input("How many questions do you want to be asked? > "))
            x = ctr # To keep track of the original number of questions desired
            answeredWrong = []
            for j in newTest:
                if ctr == 0:
                    break
                print("-"*10)
                if not j.askQuestion(): #If the answer was wrong
                    answeredWrong.append(j) #Append the answer to a wrong answer list
                    print("\nThis is the right answer:\n{}".format(j.ans))
                ctr -= 1
            if len(answeredWrong) > 0:
                print("Please review these questions!:\n")
                i = 1
                for k in answeredWrong:
                    print("{}.\n    {}\n    Correct Answer: {}\n"
                            .format(i,
                            str(k).replace('\n', '\n    '),
                            k.ans.replace('\n', '\n    ')))
                    i += 1
                print("YOU GOT {} / {} ! {:.2f}%!"
                .format(x - len(answeredWrong), x, (x- len(answeredWrong))/x))
            else:
                print("YOU WIN ALL OF THE QUESTIONS! YAY!")
    else:
        print("Usage: python hts.py [filename(s)]")

if __name__ == "__main__" : takeExam(sys.argv[1:]) # element 0 only interesting if you want the name of your file...
