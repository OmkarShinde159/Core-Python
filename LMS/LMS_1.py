
from datetime import datetime
from LMS_class import *
from LMS_decorators import *



while True:
    @show_content
    def show_welcome():
        welcome()
    show_welcome()

    # print(
    #     """
    # ... LIBRARY MANAGEMENT SYSTEM ...
    
    # 1. Admin Signup
    # 2. Admin Login
    # 3. Student Logins
    # 4. About LMS
    # 5. Exit
    # """
    # )

    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        email = input("Enter admin email: ")
        a_pwd = input("Create password: ")
        admin = [email, a_pwd]
        Admin.verify_admin(LMS, admin)

    elif choice == 2:
        login_id = input("Enter admin email: ")
        password = input("Enter admin password: ")
        if [login_id, password] in LMS.admin_log:
            print("\nAdmin login successful...!")

            while True:
                @show_content
                def show_admin_login():
                    admin_login()
                admin_login()

                # print(
                #     """
                # 1. Student Section
                # 2. Book Section
                # 0. Back
                # """
                # )

                ch = int(input("\nEnter your choice: "))
                if ch == 1:

                    while True:
                        @show_content
                        def show_std_section():
                            student_section()
                        show_std_section()

                        # print(
                        #     """
                        # 1. Register new student
                        # 2. View all students
                        # 3. Get student by ID
                        # 4. Update Student Info
                        # 5. Delete Student
                        # 0. Back
                        # """
                        # )

                        ch = int(input("\nEnter your choice: "))
                        if ch == 1:
                            # @show_content
                            # def ask_std_info():
                            #     ask_student_info()
                            # ask_std_info()

                            std_id = input("Enter student ID: ")
                            std_name = input("Enter student Name: ")
                            std_class = input("Enter student class: ")
                            std_div = input("Enter student division: ")
                            std_contact = int(input("Enter student contact: "))
                                                    
                            std = Student(
                                std_id, std_name, std_class, std_div, std_contact
                            )
                            std.add_new_student()

                        elif ch == 2:
                            for s in Student.get_students_log(Student):
                                @show_content
                                def view_all_students():
                                    std_info(s)
                                view_all_students()
                             

                            # for s in Student.get_students_log(Student):
                            #     print(
                            #         f"""
                            #     Student ID: {s.std_id},
                            #     Student Name: {s.std_name},
                            #     Student Class: {s.std_class},
                            #     Student Division: {s.std_div},
                            #     Student Contact: {s.std_contact}
                            #     """
                            #     )

                        elif ch == 3:
                            std_id = input("Enter student ID: ")
                            s = Student.get_std_by_id(std_id)
                            if s == False:
                                print(f"Student not found for id: {std_id}")
                            else:
                                @show_content
                                def view_std_info():
                                    std_info(s)
                                view_std_info()

                                # print(
                                #     f"""
                                # Student ID: {s.std_id},
                                # Student Name: {s.std_name},
                                # Student Class: {s.std_class},
                                # Student Division: {s.std_div},
                                # Student Contact: {s.std_contact}
                                # """
                                # )

                        elif ch == 4:
                            std_id = input("Enter student ID: ")
                            std_name = input("Enter student Name: ")
                            std_class = input("Enter student class: ")
                            std_div = input("Enter student division: ")
                            std_contact = int(input("Enter student contact: "))

                            update = Student.update_std_detail(Student,std_id,std_name,std_class,std_div,std_contact)
                            if update == True:
                                print("\nStudent details updated successfully...!")
                            else:
                                print(f"\nStudent not found for id: {std_id} ")

                        elif ch == 5:
                            std_id = input("Enter student ID: ")
                            print(Student.delete_std(Student, std_id))

                        elif ch == 0:
                            break

                        else:
                            print("\nInvalid choice...")

                elif ch == 2:

                    while True:
                        @show_content
                        def show_bk_section():
                            books_section()
                        show_bk_section()

                        # print(
                        #     """
                        # 1. Add new Book
                        # 2. View all Books
                        # 3. Get book by ISBN
                        # 4. Update Book Info
                        # 5. Delete Book
                        # 0. Back
                        # """
                        # )

                        ch = int(input("\nEnter your choice: "))
                        if ch == 1:
                            title = input("Enter book title: ")
                            author = input("Enter author name ")
                            isbn = input("Enter ISBN number: ")
                            publication = input("Enter publocation: ")

                            bk = Books(title, author, isbn, publication)
                            print(bk.add_new_book())

                        elif ch == 2:
                            for s in Books.get_books_log(Books):
                                @show_content
                                def view_all_books():
                                    book_info(s)
                                view_all_books()

                                # print(
                                #     f"""
                                # Title       : {s.title},
                                # Author      : {s.author},
                                # ISBN        : {s.isbn},
                                # Publication : {s.publication},
                                
                                # """
                                # )

                        elif ch == 3:
                            isbn = input("Enter ISBN: ")
                            s = Books.get_book_by_isbn(isbn)
                            if s == False:
                                print(f"Book not found for ISBN: {isbn}")
                            else:
                                @show_content
                                def view_book_by_isbn():
                                    book_info(s)
                                view_book_by_isbn()

                                # print(
                                #     f"""
                                # Title       : {s.title},
                                # Author      : {s.author},
                                # ISBN        : {s.isbn},
                                # Publication : {s.publication},
                                
                                # """
                                # )

                        elif ch == 4:
                            isbn = input("Enter ISBN number: ")
                            title = input("Enter book title: ")
                            author = input("Enter author name ")
                            publication = input("Enter publocation: ")

                            update = Books.update_book(
                                Books, title, author, isbn, publication
                            )
                            if update == True:
                                print("\nBook details updated successfully...!")
                            else:
                                print(f"\nBook not found for ISBN: {isbn} ")

                        elif ch == 5:
                            isbn = input("Enter ISBN: ")
                            print(Books.delete_book(Books,isbn))

                        elif ch == 0:
                            break

                        else:
                            print("\nInvalid choice...")

                elif ch == 0:
                    break

                else:
                    print("\nInvalid choice...")


        else:
            print("\nEmail-ID or password is incorrect...")

    elif choice == 3:
        print(LMS.student_log)
        std_id = input("Enter student ID: ")
        std_name = input("Enter student Name: ")
        s = Student.verify_student(Student,std_id,std_name)
        if s == True:
            print("\nStudent Login Successful")

            @show_content
            def std_login():
                student_login()
            std_login()

            # print(f'''
            # 1. Get bookslog
            # 2. Search book by ISBN
            # 3. Issue book
            # 4. View your issued books
            # 5. Return book
            # 6. Logout
            # ''')

            while True:
                ch = int(input("\nEnter your choice: "))
                if ch == 1:
                    for s in Books.get_books_log(Books):
                        @show_content
                        def get_booklog():
                            book_info(s)
                        get_booklog()

                                # print(
                                #     f"""
                                # Title       : {s.title},
                                # Author      : {s.author},
                                # ISBN        : {s.isbn},
                                # Publication : {s.publication},
                                
                                # """
                                # )
                    
                
                elif ch == 2:
                    isbn = input("Enter ISBN: ")
                    s = Books.get_book_by_isbn(isbn)
                    if s == False:
                        print(f"Book not found for ISBN: {isbn}")
                    else:
                        @show_content
                        def view_book():
                            book_info(s)
                        view_book()

                        # print(
                        #     f"""
                        # Title       : {s.title},
                        # Author      : {s.author},
                        # ISBN        : {s.isbn},
                        # Publication : {s.publication},
                                
                        # """)
                    
                elif ch == 3:
                    isbn = input("Enter ISBN: ")
                    print(Books.issue_book(Books,isbn))
                    print("Book issued at: ",datetime.now())
                    
                elif ch == 4:
                    for s in Books.get_issue_books_log(Books):
                        @show_content
                        def view_issued_books():
                            book_info(s)
                        view_issued_books()

                        # print(
                        #     f"""
                        # Title       : {s.title},
                        # Author      : {s.author},
                        # ISBN        : {s.isbn},
                        # Publication : {s.publication},
                        # """
                        # )

                elif ch == 5:
                    isbn = input("Enter ISBN: ")
                    print(Books.return_book(Books,isbn))
                    print("Book returned at: ",datetime.now())

                    
                elif ch == 6:
                    print("\nSuccessfully logged out..!")
                    break
                else:
                    print("\nInvalid choice ...")



        else:
            print("\nInvalid Student ID or name")


    elif choice == 4:
        @show_content
        def about_lms_rules():
            rules_regulations()
        about_lms_rules()
       

    elif choice == 5:
        break

    else:
        print("\nInvalid choice ...")
