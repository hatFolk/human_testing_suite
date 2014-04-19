# "Library" version of the function menu example.
# Notice that we have no main() function, as we're not
# interested in this file being run itself, but just want
# to define things that can be used elsewhere.

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


