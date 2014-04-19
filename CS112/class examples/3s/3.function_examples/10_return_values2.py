

def func_1(x):
    my_list = [x, x*x, x*x*x]
    return my_list

def main():
    z = func_1(int(input("Enter (#): ")))
    print(z)
    for i in z:
        print(i)

main()

# MODS and NOTES:

# we see that lists print out square brackets and commas so that it
# looks like a list.

# Notice that we used a list as a sequence in the for-loop.  This is
# normal--we just constructed the list by hand instead of getting one
# from a call to the range() function.
