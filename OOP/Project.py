# student management system

admin = "admin"
pwd = "123"

while True:
    print('''

    !!! Welcome to Student Management System !!!

    1. Sign in
    2. Login
    3. Exit 
    ''')

    choice = input("Enter Your Choice (1/2/3) : ")

    while True:

        if choice == '1':
            print("..... Create your username and password .....")
            username = input("Set username : ")
            password = input("Set password: ")
            print("username and password created successfully !!!")
            break 


        elif choice == '2':
            print('''
                    1. user login 
                    2. admin login 
                    3. Back
                ''')

            login_choice = input("Enter Your Choice (1/2/3): ")

            while True:
                if login_choice == '1':
                    print("..... Enter your username and password .....")
                    u_name = input("Enter username : ")
                    p_word = input("Enter password: ")
                    
                    if u_name == username and p_word == password:
                        print("User Login successfull !!!")
                        break
                    #     print('''
                    #         1. Enquiry
                    #         2. Rules & Regulations
                    #         3. Logout
                    #         ''')
                    #     ch = input("Enter Your Choice (1/2/3) : ")
                    #     while True:
                    #         if ch == '1':
                    #             print('''
                    #             Course Names
                    #             1. Python
                    #             2. Software Tetsing
                    #             3. Back
                    #             ''')
                    #             info = input("Enter Your Choice (1/2/3) : ")
                        
                    #             # while True:
                    #             #     if info == '1':
                    #             #         print('''
                    #             #         Elegibility : Basic understanding of computer
                    #             #         Fees : 20 to 50k
                    #             #         Course duration : 6 months
                    #             #         ''')
                    #             #         break
                                        
                                        

                    #             #     elif info == '2':
                    #             #         print('''
                    #             #         Elegibility : Basic understanding of excel
                    #             #         Fees : 20 to 50k
                    #             #         Course duration : 6 months
                    #             #         ''')
                    #             #         break
                                        
                                        

                    #             #     elif info != '3':
                    #             #         print("Invalid choice...")
                    #             #         break
                                    
                    #                 # elif info == '3':
                    #                 #     print("Redirected to logged in page..!")
                                        
                    #             break  

                                
                    #         elif ch =='2':
                    #             print('''
                    #             **** Rules & Regulations ****

                    #             1. Students should be polite, punctual and regular.

                    #             2. Students should complete all homework given to them on time and attend all tests.

                    #             3. Students should reach the center at least 5 minutes before the class starts.

                    #             4. Students should bring all necessary stationary materials and text/workbooks.

                    #             5. Cell phones and iPods should be switched off inside the classroom.
            
                    #             ''')
                    #             break

                    #         elif ch != '3':
                    #             print("Invalid choice...")
                    #             break

                    #         elif ch == 3:
                    #             print("Redirected to logged in page ...")
                    #             break


                        
                    # else:
                    #     print("Username or password is incorrect ...")
                    # break
                        
                    elif login_choice == '2':
                        print("..... Enter admin username and password .....")
                        a_name = input("Enter username : ")
                        p_word = input("Enter password: ")
                        if a_name == admin and p_word == pwd:
                            print("Admin Login successfull !!!")
                        else:
                            print("Username or password is incorrect ...")
                        break
                        

                    elif login_choice == '3':
                        print("Back to main page")
                        break
                    
        break                  
                    


        #     else:
        #         print("Enter valid choice.... ")

        # elif choice == '3':
        #     print("Successfully Exit...!!!")
        #     break
        
# admin login
    # 1. Add new student
    # 2. view all student
    # 3. view specific student
    # 4. update student details
    # 5. delete student
    # 6. logout


# Enter your choice : 1
    # student id
    # name
    # course name
    # percentage


# Enter your choice : 2
    # display all data of all students

# Enter your choice : 3
    # Enter student id


# Enter your choice : 4
    # Enter student id

# Enter your choice : 5
    # Enter student id

# Enter your choice : 6
    # redirect to admin logged in page

# to add functionality in above options we need create class and methods

   
'''
omkar = Student(1,"omkar","python",78.89)
manisha = Student(2,"manisha","python",78.99)
pooja = Student(3,"pooja","python",88.89)

print(omkar.std_id)
print(omkar.std_name)

for i in [omkar,manisha,pooja]:
    print(i.std_id, i.std_name, i.std_crs_name, i.std_per)
'''   