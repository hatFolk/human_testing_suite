import hts, sys

def main(filename):
    exam = hts.Test(filename)
    print("{} Questions Created!".format(len(exam)))
    ctr = int(input("How many questions do you want to be asked? > "))
    x = ctr
    answeredWrong = []
    for i in exam:
        if ctr == 0:
            break
        print("-"*10)
        print("\nQuestion {}:\n".format(x - ctr + 1))
        if not i.askQuestion():
            answeredWrong.append(i)
            print("\nThis is the right answer:\n{}".format(i.ans))
        ctr -= 1
    if len(answeredWrong) > 0:
        print("You go {}/{}! {:.2f}%!".format(x-len(answeredWrong), x, (x-len(answeredWrong))/x))
        a = int(input("Export Incorrect Questions to test file?\n1. Yes\n2. No\n>"))
        if a == 1:
            filename = input("Name of file? > ")
            hts.exportTest(answeredWrong, filename)
            print("Success!")
        else:
            print("Okay!")
    else:
        print("You win!")


main(sys.argv[1])
