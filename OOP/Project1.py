
admin = "admin"
pwd = "123"

class Student:
    studentlist = list()        # static or class attribute
    def __init__(self, std_id,std_name,std_crs_name,std_per) -> None:
        self.std_id, self.std_name, self.std_crs_name, self.std_per = std_id, std_name, std_crs_name, std_per

    # creating a method to add student
    def addnewstd(self):
        Student.studentlist.append(self)
        print("Student Add Successfully !!! ")

    def getstdinfo(self):          # getter method
        return Student.studentlist  

    def getstdbyid(std_id):
        for i in Student.studentlist:
            if std_id == i.getstdid():
                return i
        return False

    def getstdid(self):
        return self.std_id

    def updatestd(self,std_id,std_name,std_crs_name,std_per):
        for std in Student.studentlist:
            if std.getstdid() == std_id:
                std.std_id = std_id
                std.std_name = std_name
                std.std_crs_name = std_crs_name
                std.std_per = std_per
                return True
        return False
    
    def updatestdname(self,std_id):
        for std in Student.studentlist:
            if std.getstdid() == std_id:
                std_name = input("Enter New Name: ")
                std.std_name = std_name
                return True
        return False
        
    def updatcrsname(self,std_id):
        for std in Student.studentlist:
            if std.getstdid() == std_id:
                std_crs_name = input("Enter New Course Name: ")
                std.std_crs_name = std_crs_name
                return True
        return False
        
    def updateper(self,std_id):
        for std in Student.studentlist:
            if std.getstdid() == std_id:
                std_per = input("Enter New Percentage: ")
                std.std_per = std_per
                return True
        return False

    def deletestd(self,std_id):
        for std in Student.studentlist:
            if std_id == std.getstdid():
                Student.studentlist.remove(std)
                return f"Student Details Deleted Successfully for student id {std_id}"
        return f"Student not found for id {std_id}"
        
    
    def verify_std_id(self):
        for std in Student.studentlist:
            if std.std_id == std.getstdid():
                return True
        return False

    def verify_contact(self,std_contact):
        if std_contact.isdigit() == True:
            print("Number Verified Successfully")
        else:
            print("Please enter valid number")

         
 
while True:
    print('''

        !!! Welcome to Student Management System !!!

        1. Sign in
        2. Login
        3. Exit 
        ''')

    choice = input("Enter Your Choice (1/2/3) : ")

    if choice == '1':
        print("..... Create your username and password .....")
        while True:
            print()
            username = input("Set username : ")
            passwd = input("Set password: ")
            if len(passwd) >= 6: #omkar@159
                p = ["@","$","#","&","_"]

                for i in p:
                    x = passwd.find(i)
                    # print(x)
                    if x!= -1:
                        password = passwd
                        print("username and password created successfully !!!")
                        break
                else:
                    print("password should have atleast 1 special character")
                    break
            else:
                print("Password should have atleast 6 characters")
                break
                
            

    elif choice == '2':
        while True:
            print('''
                1. user login 
                2. admin login 
                3. Back
                ''')

            login_choice = input("Enter Your login Choice (1/2/3): ")

            if login_choice == '1':
                    print("..... Enter your username and password .....")
                    u_name = input("Enter username : ")
                    p_word = input("Enter password: ")
                    
                    if u_name == username and p_word == password:
                        print("User Login successfull !!!")

                        while True:
                            print('''
                            1. Enquiry
                            2. Rules & Regulations
                            3. Logout
                            ''')

                            ch = input("Enter user Choice (1/2/3) : ")

                            if ch == '1':
                                while True:
                                    print('''
                                    Course Names
                                    1. Python
                                    2. Software Tetsing
                                    3. Back
                                    ''')

                                    info = input("Enter course Choice (1/2/3) : ")

                                    if info == '1':
                                        print('''
                                        Elegibility : Basic understanding of computer
                                        Fees : 20 to 50k
                                        Course duration : 6 months
                                         ''')

                                    elif info == '2':
                                        print('''
                                        Elegibility : Basic understanding of excel
                                        Fees : 20 to 50k
                                        Course duration : 6 months
                                         ''')
                                    
                                    elif info != '3':
                                        print("Invalid choice ...")

                                    else:
                                        print("Redirected to logged in page...!!!")
                                        break

                            elif ch =='2':
                                print('''
                                **** Rules & Regulations ****

                                1. Students should be polite, punctual and regular.

                                2. Students should complete all homework given to them on time and attend all tests.

                                3. Students should reach the center at least 5 minutes before the class starts.

                                4. Students should bring all necessary stationary materials and text/workbooks.

                                5. Cell phones and iPods should be switched off inside the classroom.
            
                                ''')

                            elif ch != '3':
                                print("Invalid choice...")
                                

                            else:
                                print("Redirected to login options page...!!!")
                                break
                          
                    else:
                        print("Username or password is incorrect ...")

            elif login_choice == '2':
                        print("..... Enter admin username and password .....")
                        a_name = input("Enter username : ")
                        p_word = input("Enter password: ")
                        if a_name == admin and p_word == pwd:
                            print("Admin Login successfull !!!")

                            while True:
                                print('''
                                    1. Add new student
                                    2. View all students info
                                    3. View specific student info
                                    4. Update student details
                                    5. Update specific details by id
                                    6. Delete student
                                    7. Logout
                                    ''')

                                a_ch = int(input("Enter admin choice: "))

                                if a_ch == 1:

                                    std_id = int(input("Enter student id: "))
                                    std_name = input("Enter student name: ")
                                    std_crs_name = input("Enter student's course name: ")
                                    std_per = float(input("Enter student percentage: "))

                                    a = Student.verify_std_id(Student)
                                    if a == True:
                                        print("Student Id already exist ")
                                    else:
                                        std = Student(std_id, std_name, std_crs_name, std_per)
                                        std.addnewstd()

                                elif a_ch == 2:
                                    for s in Student.getstdinfo(Student):
                                        print(s.std_id)
                                        print(s.std_name)
                                        print(s.std_crs_name)
                                        print(s.std_per)

                                elif a_ch == 3:
                                    std_id = int(input("Enter student id: "))
                                    s = Student.getstdbyid(std_id)

                                    if s == False:
                                        print("\n Sorry..Student not found for id",std_id)
                                    else:
                                        print(s.std_id)
                                        print(s.std_name)
                                        print(s.std_crs_name)
                                        print(s.std_per)

                                elif a_ch == 4:
                                    std_id = int(input("Enter student Id: "))
                                    std_name = input("Enter student name: ")
                                    std_crs_name = input("Enter student's course name: ")
                                    std_per = float(input("Enter student percentage: "))
                                    
                                    update = Student.updatestd(Student,std_id,std_name,std_crs_name,std_per)
                                    if update == True:
                                        print("Student Details updated successfully")
                                    else:
                                        print("Student Not Found for Id,",std_id)


                                elif a_ch == 5:
                                    while True:
                                        print('''
                                            1. Update Name
                                            2. Update Course Name
                                            3. Update Percentage
                                            4. Back
                                            ''')

                                        u_ch = input("Enter your choice: ")
                                        if u_ch == '1':
                                            std_id = int(input("Enter Student Id: ")) 
                                            up_name = Student.updatestdname(Student,std_id) 

                                            if up_name == True:
                                                print("Student Name updated successfully")
                                            else:
                                                print("Student Not Found for Id,",std_id)
                                            

                                        elif u_ch == '2':
                                            std_id = int(input("Enter Student Id: ")) 
                                            up_crs_name = Student.updatcrsname(Student,std_id) 

                                            if up_crs_name == True:
                                                print("Student Course Name updated successfully")
                                            else:
                                                print("Student Not Found for Id,",std_id)
                                            
                                        elif u_ch == '3':
                                            std_id = int(input("Enter Student Id: ")) 
                                            up_per = Student.updatcrsname(Student,std_id) 

                                            if up_per == True:
                                                print("Student Percentage updated successfully")
                                            else:
                                                print("Student Not Found for Id,",std_id)

                                        elif u_ch == '4':
                                            break
                                            
                                        else:
                                            print("Invalid choice ...")

                                        

                                elif a_ch == 6:
                                    std_id = int(input("Enter Student Id: "))
                                    print(Student.deletestd(Student,std_id))
                                    
                                    


                                elif a_ch != 7:
                                    print("invalid choice...")

                                else:
                                    break

                
                        

                        else:
                            print("Username or password is incorrect ...")

            elif login_choice != '3':
                print("Invalid choice ...")

            else:
                print("Redirected to main page...!!!")
                break


            

    elif choice != '3':
        print("Invalid choice ...")


    else:
        print("Successfully Exit...!!!")
        break



   