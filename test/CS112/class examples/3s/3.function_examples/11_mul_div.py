def func_1(x):
    z = x*5
    print("%d * %d = %d" % (x,5,z))
    return func_2(z)

def func_2(x):
    z = x/5
    print("%d / %d = %d" % (x,5,z))
    return z

def main():
    usr_input = int(input("Enter (#): "))
    y = func_1(usr_input)
    print("input is now: ", y)

main()

# look at func_1 and func_2.  They both have an x and a z in them. Are
# they referring to the same spots in memory (an x from each, or also
# a z from each)?
