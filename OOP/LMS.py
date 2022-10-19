"""
You have to build a library management system using Django where an admin can
perform CRUD ( create, read, update and delete) operations like
    ● Add a Book
    ● Update an entry of a book
    ● Delete a book
    ● Get all books

1. Admin Signup:
    a) Insert admin details in tables.
    b) An admin records should be unique based on email, which means
    duplicates records should not be able to enter in DB.
2. Admin Login:
    a) The Admin can log in based on email and password.
3. Create an entry for Books.
    a) The admin can create a new entry of a book.
4. Retrieve all the books.
    a) Retrieve all the books.
5. Update a book.
    a) The book records should be able to update.
6. Delete a book.
    a) The book record should be deleted
Student View:
    1. View all the records of book
Conditions:
    1. For Front end, you can use any library / framework to build the UI.
    2. Write the documentation for backend code


"""


def ask_details(func):
    std_id = input("Enter student ID: ")
    std_name = input("Enter student Name: ")
    std_class = input("Enter student class: ")
    std_div = input("Enter student division: ")
    std_contact = int(input("Enter student contact: "))


# def print_details():
#     ask_details()
#     return ask_details


# print_details = ask_details(print_details)


@ask_details
def print_details():
    ask_details()

# def std_info(func): 
#     print(f"""
#             Student ID: {s.std_id},
#             Student Name: {s.std_name},
#             Student Class: {s.std_class},
#             Student Division: {s.std_div},
#             Student Contact: {s.std_contact}
#             """
#             )

# @std_info
# def add_std_info():
#     std_info()