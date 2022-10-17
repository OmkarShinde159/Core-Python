# create a table of 2 to 100 only , if not print num is out of range-------------------------------------------


num = int(input("Enter the number to print its multiplication table : "))

# method 1
if num >1 and num<=100:
    num1 = 1
    print("Multiplication table of",num)
    while num1 < 11:
        print(num,"*",num1,"=",num*num1)
        num1 += 1

else:
    if num <= 0 or num > 100:
        print("Number is out of range")

# method 2
if num>0:
    if num <101:
        i = 1
        while i <= 10:
            print(num,"*",i,"=",num*i)
            i = i+1
    else:
        print("out of range")

else:
    print("Negative Number")
