# if-elif-else structure.

grade = float(input("What is your current score in the class? "))

if (grade >=90):
    print ("congrats, you're getting an A! You star student, you.")
elif (90 > grade >= 80):
    print ("good work! you're getting a B.  Solid effort.")
elif (80 > grade >= 70):
    print (" okay, you're getting a C.  At least you won't need to re-take the course, yeah?")
elif (70 > grade >= 60):
    print ("uh-oh, your grade is a D. I hope there's still time to work up to a higher grade!")
else:
    print ("That score is a failing grade.  ;(")


# MODIFICATIONS:

# add code that figures out if the user entered
# a number over 100 or under zero, and print 
# messages for those too.  (handling error cases
# is important!)

# make the out-of-bounds check (from prev. mod.)
# the `outermost' if-stmt, and put the entire 
# if-elif-else block inside of it. What are the
#  pros/cons here?

# think about the order of the conditional 
# statements; how can we simplify our boolean
# expressions? Make them simpler.
