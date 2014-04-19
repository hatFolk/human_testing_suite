
def func_1():
    print("...in func_1...")
    func_2()

def func_2():
    print("...in func_2...")

def main():
    print("...in main...")
    func_1()
    print("done.")

main()


# NOTES:

# if we deleted all the print statements, the same control flow would
# occur--we just wouldn't have visual reminders of it.


