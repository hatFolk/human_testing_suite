def func_1(text1):
    print(text1 + "(" + str(id(text1)) + ")...in func_1")
    text3 = func_2(text1)
    print(text3 + "(" + str(id(text3)) + ")...back in func_1...")
    return text3

def func_2(text2):
    print(text2 + "(" + str(id(text2)) + ")...in func_2...")
    return text2

def main():
    text0 = "id:"
    print(text0 + "(" + str(id(text0)) + ")...in main...")
    text4 = func_1(text0)
    print(text4 + "(" + str(id(text4)) + ")...back in main...")


main()

# What does the id function do?

# add a variable assignment as the first line of main(),
# just to see the effect on the id function's output.
