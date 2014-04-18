

x = 10    # defined at global (module) scope level

def func_1():
    x = 20  # defined at local (sub-level) scope
    print("in func_1, x =",x)

def func_2():
    global x  # specifies access to the global variable x
    x = 20
    print("in func_2, x =",x)


def main():
    print("initially, x =",x)
    func_1()
    print("after func_1, x =",x)
    func_2()
    print("after func_2, x =",x)
    

main()


# NOTES: 

# func_1 has its own variable named x that is NOT THE SAME as the
# global x. The x=20 statement creates a local varable named x.

# func_2 explicitly uses the global version of x. the x=20 statement
# doesn't create a local variable x.

# main implicitly uses the global version of x.  It never assigns to
# x, so we didn't need to state "global x" as we did in func_2.

# SCOPE

# The scope of global x is the entire file (as long as x=10 has been
# executed before we try to run the function that accesses this global
# x). The scope of func_1's x, however, is just inside that
# function. Once we leave func_1, that local x 'dies' (falls out of
# scope), and is no longer stored in memory and can't be accessed any
# more.
