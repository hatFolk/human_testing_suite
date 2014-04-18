num = int (input ("number please: "))

if num>=90:
    print("A!")
    num = num - 10
elif 90 > num >=80:
    print ("B")
    num = num - 9
elif 80> num >=70:
    print ("C")
    num = num - 8
elif 70 > num >=60:
    print ("D")
    num = num - 7
else : # covers (num <= 60)
    print ("F")

print("done.")
