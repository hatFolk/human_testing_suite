# example from the slides.  We make each option and task of our
# menu into a function, so that the main() function is much easier
# to read, and is more abstract (gets to ignore the details).


# define a function, print_menu, that prints a menu
# (and does nothing else).
def print_menu():
    print("-----MENU-----\n\n")
    print(" (1)- Add\n")
    print(" (2)- Subtract\n")
    print(" (3)- Quit\n\n")
    print("Select (x,#,#): ")

# defines a function, add_func, which adds its two parameters.
def add_func(op_1, op_2):
    return (op_1  + op_2)

# defines a function, sub_func, which subtracts its two parameters.
def sub_func(op_1, op_2):
    return op_1 - op_2

# defines a function, format_and_print, which formats
# and prints its parameters.  This function helps hide
# all the untidy details of the special formatting.
def format_and_print(sign,op_1,op_2,result):
    print("\n%d %s %d = %d\n" % (op_1,sign,op_2,result))

# define what our program shoud do.
def main():
    option = -1 # any option other than 3...

    while option !=3:
        print_menu()
        option,op_1,op_2 = eval(input())
        if option==1:
            result = add_func(op_1,op_2)
            sign = "+"
        elif option==2:
            result = sub_func(op_1,op_2)
            sign = "-"
        elif option==3:
            print("Goodbye...")
        else:
            print("Mistake...\n")

        # print out our results when requested.
        if option==1 or option==2:
            format_and_print(sign,op_1,op_2,result)


# run our program.
main()


# MODS and Qs:

# we used op_1 and op_2 everywhere; this is not required.
# Try renaming op_1 and op_2 just in the main function
# without breaking the code.

# Similarly, use different variable names in 
# sub_func and add_func.

# using input to grab multiple values is cool, but also
# forces the user to enter a menu option and two numbers 
# even when they want to quit (e.g., "3,1,1" instead of "3").
# change the code so that the menu option is selected first,
# and then we get the pair of numbers from the user.
