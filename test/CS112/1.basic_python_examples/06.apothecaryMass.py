# from http://ts.nist.gov/weightsandmeasures/publications/appxc.cfm

# Apothecary Units of Mass:

# 12 ounces  = 1 pound
# 8 drams    = 1 ounce
# 3 scruples = 1 dram
# 20 grains  = 1 scruple


# Ask the user for the number of pounds.  Tell them how many scruples and grains.

numPounds   = int(input ("how many pounds ya got? "))
numOunces   = 12 * numPounds
numDrams    =  8 * numOunces
numScruples =  3 * numDrams
numGrains   = 20 * numScruples


print ("if you've got "+str(numPounds)+" pounds, you've got:")
print (str(numScruples)+" scruples")
print (str(numGrains)+" grains")




