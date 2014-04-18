# Simple if-statement example.  

# By running the code multiple times, and entering 
# 10 sometimes and a different number other times,
# we see that the body of the if-statement only runs
# precisely when (input==10) is true when the if-stmt
# is reached.

# get a guess from the user.
guess = int(input( "Let's play the Guess Ten Game!  Guess Ten.  "))

# check their guess. When it's true their guess is 
# correct, run the code block.
if (guess==10):
    print ("Hooray, you guessed ten!")

print ("Thanks for playing this easy, easy game.")
