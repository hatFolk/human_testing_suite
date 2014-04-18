# while-loop example.

# no matter how many times they incorrectly guess
# the password, we can always handle another guess.

# initialize (set) the password and any guess that
# doesn't equal the password. This ensures we run the 
# while-loop at least once.
password = "mason"
guess = ""

# while they don't have the correct password, get 
# a new guess.

tries = 0

while (guess != password):
    print ("You need to correctly guess the password.")
    guess = input ("what is the password? ")
    tries += 1
    if tries >=5:
        break
    print("end of loop body this time...")

print ("Hooray, you are indeed a super secret member"\
      +" of our super secret club.")
