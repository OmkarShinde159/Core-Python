# accept only positive number and give its factorial.and if user enter negative number
# display we cannot find factorial or negative number, and if user enter number
# greater than 100 print out of range, and if user enter 0 display enter numbered is zero
#------------------------------------------

fact = 1
num = int(input("Enter Number to find its factorial: ")) #say 5
if num > 0 and num <= 100:
    while num >= 1:# 5 4 3 2 1 false
        fact = fact * num
        num -= 1
    print("Factorial is : ",fact) 
elif num < 0:  
    print("cant find factorial, enter number greater than 0")
elif num > 100:
    print("num is out of range")
else:
    print("Number is zero")
