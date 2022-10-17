user1 = "omkar.shinde159"
user2 = "8108102895"
passward = "123"

print("Enter 1 for login")
print("Enter 2 for sign up")

ch = input("Enter Your Choice: ")

if ch == '1':

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


elif ch == '2':
    
    user1 = input("Set username: ")
    user2 = input("Enter mobile no: ")
    passward = input("Set Passward: ")
    print("Username & Passward created succefully")

    print("Enter 1 for Login")
    print("Enter 2 for Exit")
    ch = input("Enter your choice: ")

    if ch=='1':
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

    elif ch=='2':
        print("Exit Succesful")

    else:
        print("----Invalid Choice---")

else:
    print("----Invalid Choice---")


        
        
    

    
'''

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


'''
