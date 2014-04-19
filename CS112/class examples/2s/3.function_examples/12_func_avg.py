
def average(my_list):
    x=0
    for i in my_list:
        x += i
    return float(x) / len(my_list)


def main():
    # [ ] represents the empty list.
    my_list=[ ]

    for i in range(3):
        # the append method adds an element to a list.
        my_list.append(int(input("(Enter (#): ")))
    
    # %0.1f gives even more formatting info.
    print("Avg = %0.1f"  %  average(my_list))


main()

# MODS and NOTES:

# Recall what %0.1f means.  (try entering 5,5,6.  Compare with
# (5+5+6)/3.0. )

# change the numbers in %0.1f, and see what happens.

# think about how to ask the user for how many numbers they want
# averaged, and how to do that in the code rather than always
# averaging three numbers.  --> where does the code change?  Where
# *doesn't* the code change?
