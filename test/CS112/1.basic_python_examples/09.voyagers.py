# data from http://voyager.jpl.nasa.gov/mission/weekly-reports/index.htm
# exercise adapted from Intro to Computing in Python text.

# Voyager 1 was 18,098,000,000 km from the Earth on 8/3/2012.
# NASA launched it on September 5, 1977!
# radio waves in space travel at the speed of light: 299,792,458 m/s

# how long would it take a radio message to travel from Voyager 1 back to earth?
# dist(m) = speed(m/s) * time(s).  Solve for time.


# dist_km is in kilometers: 18,098,000,000.
dist_km = 18098000000

# speed is in m/s
speed = 299792458

# transitTime is in seconds
transitTime = (dist_km*1000) / speed

# print all that information to the user.
print ("as of 8/3/2012, Voyager 1 was " + str(dist_km)
       + "km away from Earth. Radio waves traveling" \
       + " at the speed of light ("+str(speed)+" m/s)"\
       + " would take " + str(transitTime) \
       + " seconds to phone home from Voyager 1.")

# MODIFICATIONS:
# translate seconds to minutes, hours, days.


