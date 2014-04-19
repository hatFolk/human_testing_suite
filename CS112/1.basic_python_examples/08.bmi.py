# BMI, or "body mass index" roughly correlates with more accurate measurements of body fat.

# bmi = weight(kg) / (height(m) ** 2)

# 12 inches in a foot, 2.56 centimeters in an inch.
# 100 centimeters in a meter.

# 2.2 pounds = 1 kilogram


# ask user for their height as a single float number:
heightFeet = float(input ("What is your height in feet? (use decimal point for inches): "))
heightMeters = heightFeet * 12 * 2.54 / 100

# ask user for their weight in pounds:
weightPounds = float(input ("What is your weight in pounds? "))
weightKilograms = weightPounds / 2.2

# calculate the BMI.
bmi = weightKilograms / (heightMeters ** 2)

print ("your BMI is: " + str(bmi))

# MODIFICATIONS:
# ask for feet and inches separately (easier on the user).
