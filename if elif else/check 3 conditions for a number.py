# 4. nested if else
# WAP to check 3 condions of a number

num = int(input("Enter Number: "))

# case 1
if num <= 100:
    if num >= 50:
        print("Number is between 50 and 100")
    else:
        print("Number is less than 50")
else:
    print("Number is greater than 100")

# case 2
if num > 0:
    print("Positive Number")
else:
    if num < 0:
        print("Negative Number")
    else:
        print("Number is Neutral")
