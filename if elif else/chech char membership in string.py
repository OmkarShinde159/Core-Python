2.   
# take string and character from user and check if 
# given char is present in given string or not

s1 = input("Enter a string: ")
string = s1.lower()
s2 = input("Enter char to check: ")
char = s2.lower()
if char in string:
    print(s2," is present in ",s1)
else:
    print(s2," is not present in ",s1)

#---------------------------------------------------------------------

1.
# WAP to check if y is present in "hello" or not.
s = "hello"
if "y" in s:
    print("y is present in hello")
else:
    print("y is not present in hello")
