# WAP TP calculate percentage and given grade according
# to percentage and take marks from the user

maths = int(input("Enter the marks, Maths: "))
science = int(input("Enter the marks, Science: "))
history = int(input("Enter the marks, History: "))
hindi = int(input("Enter the marks, Hindi: "))
marathi = int(input("Enter the marks, Marathi: "))

marks = maths + science + history + hindi + marathi 
total = 500

perc = marks/total*100
print("Percentage is: ", perc)

# 0-100
# A - 90 above
# B - 81 - 89.99
# C - 71 - 80
# D - 61 - 70
# E - 51 - 60
# F - 35 - 50
# Fail - Below 34

if perc>=90:
    print("A Grade")
elif perc>80 and perc<90:
    print("B Grade")
elif perc>70 and perc<=80:
    print("C Grade")
elif perc>60 and perc<=70:
    print("D Grade")
elif perc>50 and perc<=60:
    print("E Grade")
elif perc>=35 and perc<=50:
    print("F Grade")
else:
    print("Failed")
