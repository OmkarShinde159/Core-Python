#WAP to print "Login Successful" only if entered username and passward are
# correct if not correct print"please try again"
# username = SquadOnline
# Passward = 123

user1 = "omkar.shinde159"
user2 = "8108102895"

passward = "123"

userInput = input("Enter username: ")

# case1
if userInput == user1 or userInput == user2:
    pw = input("Enter passward: ")
    if pw == "123":
        print("Login Successful")
    else:
        print("Please enter valid passward")
else:
    print("Please enter valid username")          
    

# case2
userInput = input("Enter username: ")
pw = input("Enter passward: ")
if userInput == user1 or userInput == user2 and pw == passward:
    print("Login Successful")
elif userInput == user1 or userInput == user2 and pw != passward:
    print("Invalid Passward ! Please Try Again !")
elif userInput != user1 or userInput != user2 and pw == passward:
    print("Invalid Username ! Please Try Again !")
else:
    print("Invalid Username & Passward ! Please Try Again !")
 
