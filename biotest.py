import hts, sys

def exportWrong(xs):
    filename = input("Name of file? > ")
    test = open(filename, "w")
    x = ""
    for i in xs:
        x += (i.question+"\n\n\n"+"***"+i.ans+"\n")
        for j in i.choice.choices.values():
            if j != i.ans:
                x+=("***"+j+"\n")
        x+=("\n\n")
    test.write(x[:-3])
    test.close()
    print("Success!")


def main(filename):
    exam = hts.Test(filename)
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
            exportWrong(answeredWrong)
        else:
            print("Okay!")
    else:
        print("You win!")


main(sys.argv[1])
