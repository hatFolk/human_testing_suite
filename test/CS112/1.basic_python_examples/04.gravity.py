
# earth's radius: 6378x10^3 meters
# earth's mass: 5.9742*10^24 kg
# user's mass: input in kg
# Universal Gravitational Constant: G=6.67300*10^(-11)

#     F = G(m1)(m2)/(r**2)


radius = 6378e3        # meters
earthMass = 5.9742e24  # kilograms
myMass = float(input("how many kilograms do you weigh? (roughly equals pounds/2.2)"))
univGravConst = 6.673e-11  # (m**3)(kg**-1)(s**-2)

force = univGravConst * earthMass * myMass / (radius**2)

print ("force = " + str(force) + " m*kg/(s**2).")

# F = mg, so g = F/m.

gravity = force / myMass

print ("gravity is " + str(gravity) + " m/(s**2).")


# MODIFICATIONS:
# change the math and prompt to let the user enter pounds instead of kilograms. (Still report in kg).
