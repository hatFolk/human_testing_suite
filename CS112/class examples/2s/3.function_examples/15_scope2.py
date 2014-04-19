
def func_1():
    x = 20  # defined at local (sub-level) scope
    print("in func_1, x =",x)

def func_2():
    global x  # specifies access to the global variable x. Does it exist yet?
    x = 20
    print("in func_2, x =",x)

def func_3():
    # x wasn't declared here but we read its value...  what does
    # Python choose for it?
    print("in func_3, x =",x) 


def main():
    x = 10  # local x?
    print("initially, x =",x)
    func_1()
    print("after func_1, x =",x)
    func_2()
    print("after func_2, x =",x)
    func_3()
    print("after func_3, x =",x)
    

main()

# SCOPE

# func_2 *creates* the global variable named x, and gives it a value.

# func_3 then accesses that global variable x implicitly. (no "global
# x" statement).

