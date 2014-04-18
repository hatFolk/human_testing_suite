# a single star means that the function accepts unlimited parameters,
# and it will pack them into a tuple with the given parameter name.
def f1 (*xs):
    print("\nf1.")
    for x in xs:
        print (x)

#we can have extra arguments before the star-param.
def f2 (a, *xs):
    print("\n\nf2.",type(xs))
    if a:
        xs = reversed(xs)
    for x in xs:
        print (x)
    
# double star means accept named arguments; pack them all into a
# dictionary of given name.
def f3(**keyparams):
    print ("\nf3")
    for k in keyparams:
        print (k, keyparams[k])

def f4(a,b,c,d,e):
    print ("\nf4")
    print (a,b,c,d,e)

def f5(z,x,y):
    print("\nf5")
    print(x,y,z)

def main():
    f1(1,2,3,4,5)
    f2(True, 1,2,3,4,5)
    f2(False, 1,2,3)
    f2(False)
    f3(a=1, b=2, c=3)

    # we can also use stars when calling params.
    nums = [1,2,3,4,5]
    tnums = (1,2,3,4,5)
    d = {"x":1,"y":2, "z":3}
    
    # f4 expects 5 args, we 'unpack' them from our single nums list.
    f4(*nums)
    f4(*tnums)
    f5(**d)
    
    # but be careful: we must have exactly the needed keyword args,
    # and no others.

    d2 = {"x":1,"y":2, "z":3, "w":4}
    # f5(**d2) # error

main()

# NOTES

# We always see a single star next to a list or tuple, and the result
# is the same as if we had written out all of its elements in order
# instead.

# We always see a double star next to what should be a dictionary, and
# the result is as if we had written out each of its key-value pairs
# in "keyword argument" (or "keyword parameter") style instead.

# be sure you understand how to use these both at the function
# declaration and at the function call site.

