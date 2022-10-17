

class LMS:
    admin_email = list()
    
    admin_book_list = list()
    def __init__(self,isbn,title,author,language,publisher) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        self.language = language
        self.publisher = publisher
        
    def add_new_admin(self):
        LMS.admin_email.append(self)
        print("Admin added Successfully !")

    def get_admin_info(self):
        for user in LMS.admin_email:
            print(user)


    def add_new_book(self):
        LMS.admin_book_list.append(self)
        print("New Book Added Successfully.\n")

    def get_books_info(self):
        return LMS.admin_book_list

    def get_isbn(self):
        return self.isbn

    def get_book_by_isbn(isbn):
        for book in LMS.admin_book_list:
            if isbn == book.get_isbn():
                return book
        return False

    def verify_isbn(self):
        for book in LMS.admin_book_list:
            if book.isbn == book.get_isbn():
                return True
        return False    

   
    def update_book(self,isbn,title,author,language,publisher):
        for bk in LMS.admin_book_list:
            if bk.get_isbn() == isbn:
                bk.isbn = isbn
                bk.title = title
                bk.author = author
                bk.language = language
                bk.publisher = publisher            
                return f"Book of ISBN {isbn} Updated successfully\n"
        return f"Book not found of ISBN: ,{isbn}\n"

    def delete_book(self,isbn):
        for bk in LMS.admin_book_list:
            if isbn == bk.get_isbn():
                LMS.admin_book_list.remove(bk)
                return "Book deleted successfully..!"
        return "Invalid ISBN..."



while True: 
    print('''

    !!! Welcome to Library Management System !!!

    1. Admin Signup
    2. Admin Login
    3. View All Admins
    4. Exit 
    ''')

    choice = int(input("Enter Your Choice (1/2/3) : "))

    if choice == 1:
        print("..... Create username and password .....")
        while True:
            print()
            
            username = input("Enter Email-ID : ")
            passwd = input("Set password: ")
            if len(passwd) >= 6: 
                p = ["@","$","#","&","_"]
                for i in p:
                    x = passwd.find(i)
                    # print(x)
                    if x != -1:
                        password = passwd
                        if username in LMS.admin_email:
                            print("User already exist, Try another username !")
                        else:
                            LMS.admin_email.append(username)
                            print("username and password created successfully !!!")
                        break
                          
                else:
                    print("password should have atleast 1 special character")
                break
                
            else:
                print("Password should have atleast 6 characters")
                break

    elif choice == 2:
        u_name = input("Enter Email-ID : ")
        p_word = input("Enter password: ")
        print()
        if u_name in LMS.admin_email and p_word == password:
            print("Admin Login Successful !!!\n")


            while True:
                print(" 1. Create a new emtry of book ")
                print(" 2. Retrive all the books")
                print(" 3. Update book record")
                print(" 4. Delete book")
                print(" 5. Back\n")

                select = int(input("Enter your choice: \n"))

                if select == 1: # new book
                    isbn = input("Enter ISBN Number: ")
                    title = input("Enter Book Title: ")
                    author = input("Enter Author Name: ")
                    language = input("Enter Language: ")
                    publisher= input("Enter Publisher Name: ")

                    var = LMS.verify_isbn(LMS)
                    if var == True:
                        print("ISBN already exists...!\n")
                    else:
                        new = LMS(isbn, title, author, language, publisher)
                        new.add_new_book()
                    
                elif select == 2:   # get all books
                    for bk in LMS.get_books_info(LMS):
                        if True:
                            print(f"ISBN Number:\t{bk.isbn} \nTitle:\t\t{bk.title} \nAuthor:\t\t{bk.author} \nLanguage:\t{bk.language} \nPublisher:\t{bk.publisher} \n")
                    else:
                        print("No Record Found\n")
                        
                elif select == 3:   # update book by ISBN
                    isbn = input("Enter ISBN Number: ")
                    title = input("Enter Book Title: ")
                    author = input("Enter Author Name: ")
                    language = input("Enter Language: ")
                    publisher= input("Enter Publisher Name: ")

                    update = LMS.update_book(LMS,isbn,title,author,language,publisher)
                    print(update)
                  
                elif select == 4:   # delete book
                    isbn = input("Enter ISBN Number: ")
                    delete = LMS.delete_book(LMS,isbn)
                    print(delete)

                    
                elif select == 5:   # back
                    break

                else:   # invalid choice
                    print("Invalid choice...")
                    
        else:
            print("Enter Valid Email-ID or Password ...")

    elif choice == 3:
        LMS.get_admin_info(LMS)
    
    
    elif choice == 4: # exit
        break

    else:   # invalid choice
        print("Invalid choice...")
    
    



