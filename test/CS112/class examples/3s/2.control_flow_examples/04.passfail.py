# if-else control structure, including nesting.


score = float(input("What is your current percentage grade in the class?"))

if (score>=60):
    print ("congratulations, you are passing.")
    if (score<70):
        print ("... but you're getting a D, so you might not be too excited about it.")
else:
    print ("sorry, you are failing this course. :(  I hope there's enough time to do better!")


# Notice that we can have control structures
# inside of control structures. When we get to the
# nested if, we already know that score>=60. We further
# check if score<70.

# MODIFICATIONS:

# using just if-else statements, print separate messages
#  for each grade (A,B,C,D,F).  --> we will find a 
# better (clearer) way to do this soon!

# use the <= and > operators (instead of >= and <) 
# to achieve the same result.

