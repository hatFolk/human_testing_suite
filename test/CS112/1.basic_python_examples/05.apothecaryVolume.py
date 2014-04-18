# from http://ts.nist.gov/weightsandmeasures/publications/appxc.cfm

# Apothecary Units of Liquid Volume:

# 4 quarts     = 1 gallon
# 2 pints      = 1 quart
# 16 fl. ounce = 1 pint
# 8 fl. drams  = 1 fl. ounce
# 60 minims    = 1 fluid dram

# Ask the user for the number of gallons.  Tell them how many drams and minims.

numGallons = int(input ("how many gallons ya got? "))
numQuarts  = numGallons *  4
numPints   = numQuarts  *  2
numOunces  = numPints   * 16
numDrams   = numOunces  *  8
numMinims  = numDrams   * 60

print (str(numGallons)+" gallons is equivalent to "\
           +str(numDrams)+" fluid drams, or "\
           +str(numMinims)+" fluid minims."
       )

