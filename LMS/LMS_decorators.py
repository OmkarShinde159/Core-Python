
from LMS_class import LMS,Admin,Student,Books


def show_content(func):
    def wrapper_func(*args):
        func(*args)

    return wrapper_func


def welcome():
    print(
        """
    ... LIBRARY MANAGEMENT SYSTEM ...
    
    1. Admin Signup
    2. Admin Login
    3. Student Login
    4. About LMS
    5. Exit
    """
    )


# welcome()


def admin_login():
    print(
        """
    1. Student Section
    2. Book Section
    0. Back
    """
    )


# admin_login()


def student_section():
    print(
    """
    1. Register new student
    2. View all students
    3. Get student by ID
    4. Update Student Info
    5. Delete Student
    0. Back
    """
    )

def books_section():
    print("""
    1. Add new Book
    2. View all Books
    3. Get book by ISBN
    4. Update Book Info
    5. Delete Book
    0. Back
    """)

def student_login():
    print(f'''
    1. Get bookslog
    2. Search book by ISBN
    3. Issue book
    4. View your issued books
    5. Return book
    6. Logout
    ''')

def std_info(s):
    print(f"""
    Student ID: {s.std_id},
    Student Name: {s.std_name},
    Student Class: {s.std_class},
    Student Division: {s.std_div},
    Student Contact: {s.std_contact}
    """
    )

def book_info(s):
    print(f"""
    Title       : {s.title},
    Author      : {s.author},
    ISBN        : {s.isbn},
    Publication : {s.publication},
                                
    """)
    
    
def ask_student_info():
    std_id = input("Enter student ID: ")
    std_name = input("Enter student Name: ")
    std_class = input("Enter student class: ")
    std_div = input("Enter student division: ")
    std_contact = int(input("Enter student contact: "))

    return std_id,std_name,std_class,std_div,std_contact

def rules_regulations():
    print('''
    1. Library users must prominently display their Student ID on them at all times. 
    2. Students who fail to do so will not be allowed access to the Library facilities.
    3. No items belonging to the library are to be taken out of the library unless they have been checked out at the Circulation Desk.
    4. Personal belongings should not be left unattended. The library management will not be held responsible for the loss of personal belongings.
    5. No food and drink (except plain water) are allowed in the library.
    6. Mobile phones or any other personal electronic gadgets must be switched to silent mode before entering the library.
    7. Making unreasonable noise, loud conversations, loud cell phone calls or playing loud music or video that can distract other library users in the library is not permitted.
    8.Users are prohibited from making or answering calls within the quiet zone.
    9. Discussion room is used for academic purposes only and should not be used for private study or social purposes.
    10. Eating, drinking, sleeping and smoking are not allowed in the library.
    11. The Library users should be professionally attired, as specified in the student handbook. We reserve the right to deny entry to students who are inappropriately attired.
    12. Library furniture/equipment should not be moved from its original location.
    13. Personal Computers provided are to be strictly used for academic research and Library CD viewing only. These computers cannot be used for personal e-mail, online chatting or playing games.
    14. Library staffs reserve the right to inspect bags or other personal property when users enter or leave the library.
    15. When a user is caught for breaching the library rules and regulations, immediate action will be taken.
''')

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_whee():
#     print("Whee!")

# say_whee()
