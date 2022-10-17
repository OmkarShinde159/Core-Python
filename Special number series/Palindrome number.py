# WAP to check if number is palindrome or not
# 432 - 232
# 121 - 121
num = int(input("Enter the number to check: "))
temp = num
rn = 0
while num>0:
    p = num%10
    rn = rn*10+p
    num = num//10
print(rn)
if temp == rn:
    print("yes",temp,"is a palindrome number")
else:
    print("No",temp,"is not a palindrome number")
    
