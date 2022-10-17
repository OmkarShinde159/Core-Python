#WAP to calculate percentage using obtaining marks
# formula: (obtained marks/total marks)*100

total = int(input("Enter the total marks: "))
maths = int(input("Enter the marks obtained in maths: "))
english = int(input("Enter the marks obtained english: "))
history = int(input("Enter the marks obtained history: "))



obtained_marks = maths + english + history
print("obtained marks is : ", obtained_marks,"/",total)
perc = (obtained_marks/total)*100
print("Your percentage is: ", perc)
print(type(perc))
