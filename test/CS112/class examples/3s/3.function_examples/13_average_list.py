

def average(my_list):
    sum = 0
    for i in my_list:
        sum += i
    return float(sum) / len(my_list)


def main():
    
    numbers1 = list(range(0,10))
    avg1 = average(numbers1)
    print("average %d: %0.1f" % (1,avg1))
    
    avg2 = average([1,4,3,5,7,6,2])
    print("average %d: %0.1f" % (2,avg2))
    
    avg3 = average([3])
    print("average %d: %0.1f" % (3,avg3))
    

main()

# NOTES and MODS:

# it feels like we could actually give average() different numbers of
# params, but really it's always one: a tuple.


# change the average function to use a "Polymorphic Formal Parameter".
# Change the function calls to average to use this new and simpler
# calling convention.

# handle the divide-by-zero issue (arises when we pass the empty
# list).
