# if users enter number is positive then accept upto 50
# and then print numbers from 1 to users entered umber
# if user number is beound 50 then print out of range
# if number is negative print number is negative

num = int(input("Enter num: "))

if num > 0 and num <= 50:
    i = 1
    while num >= i: 
        print(i)
        i += 1
elif num > 50:
    print("Out of range")
elif num == 0:
    print("number is zero")
else:
    print("Number is negative")
