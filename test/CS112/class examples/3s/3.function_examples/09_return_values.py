
def func_1(x):
    return x, x*x, x*x*x

def main():
    a,b,c = func_1(int(input("Enter (#): ")))
    print(a,b,c)

main()

# NOTES and MODs:

# multiple assignments and multiple return values are actually just
# tuples.  Try adding parentheses to func_1's return statement, and to
# main's assignment, to express them as tuples.

