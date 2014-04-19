# func_menu_lib.py contains the contents of 05_func_menu.py,
# except that it does not have a main() method (or main() call).
# 
# While it's convenient to number our code samples, python needs a
# valid identifier as the file name.  so we had to store it in
# something that didn't start with a number, and the name
# func_menu_lib was chosen.
import func_menu_lib


# define what our program shoud do.
def main():
    print("Using Imported Functions.\n\n")
    option = -1 # any option other than 3...

    while option !=3:
        func_menu_lib.print_menu()
        option,op_1,op_2 = eval(input())
        if option==1:
            result = func_menu_lib.add_func(op_1,op_2)
            sign = "+"
        elif option==2:
            result = func_menu_lib.sub_func(op_1,op_2)
            sign = "-"
        elif option==3:
            print("Goodbye...")
        else:
            print("Mistake...\n")

        # print out our results when requested.
        if (option==1 or option==2):
            func_menu_lib.format_and_print(sign,op_1,op_2,result)


# run our program.
main()

# By importing func_menu_lib.py's contents, we had to *qualify* each
# use of each named thing from that file.  We can also import those
# things *unqualified*, if we're okay with the names all inhabiting
# our module's "namespace".  Change the import statement to:
# 
#  from func_menu_lib import *
# 
# , and remove all qualifications so the code works again.

# --> What are the pros/cons of each implementation?
