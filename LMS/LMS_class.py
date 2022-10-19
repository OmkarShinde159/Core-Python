class LMS:
    admin_log = list()
    student_log = list()
    books_log = list()
    issue_books_log = list()


class Admin(LMS):
    def add_admin(self):
        LMS.admin_log.append(self)
        print(LMS.admin_log)
        print("Admin added Succesfully ...!")

    def verify_admin(self, admin):
        if LMS.admin_log != []:
            for e in LMS.admin_log:
                while True:
                    if e[0] in admin:
                        print("Email already exist, Try using another email...!")
                        break
                    else:
                        Admin.add_admin(admin)
                        # print("In while loop")
                    break
                break
        else:
            Admin.add_admin(admin)
            # print("In outer if")




class Student(LMS):
    def __init__(self, std_id, std_name, std_class, std_div, std_contact) -> None:
        super().__init__()
        self.std_id = std_id
        self.std_name = std_name
        self.std_class = std_class
        self.std_div = std_div
        self.std_contact = std_contact

    def verify_student(self, std_id, std_name):
        for ob in Student.student_log:
            if ob.get_std_id() == std_id:
                if ob.get_std_name() == std_name:
                    return True
        return False

    def add_new_student(self):
        Student.student_log.append(self)
        print("Student registered successfully...!")

    def get_students_log(self):
        return Student.student_log

    def get_std_id(self):
        return self.std_id

    def get_std_name(self):
        return self.std_name

    def get_std_by_id(std_id):
        for i in Student.student_log:
            if std_id == i.get_std_id():
                return i
        return False

    def update_std_detail(self, std_id, std_name, std_class, std_div, std_contact):
        for std in Student.student_log:
            if std.get_std_id() == std_id:
                std.std_id = std_id
                std.std_name = std_name
                std.std_class = std_class
                std.std_div = std_div
                std.std_contact = std_contact
                return True
        return False

    def delete_std(self, std_id):
        for std in Student.student_log:
            if std_id == std.get_std_id():
                Student.student_log.remove(std)
                return f"Student Details Deleted Successfully for student id {std_id}"
        return f"Student not found for id {std_id}"



class Books(LMS):
    def __init__(self, title, author, isbn, publication) -> None:
        super().__init__()
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication = publication

    def add_new_book(self):
        Books.books_log.append(self)
        return f"\nAdded new book...!"

    def get_books_log(self):
        return Books.books_log

    def get_isbn(self):
        return self.isbn

    def get_book_by_isbn(isbn):
        for i in Books.books_log:
            if isbn == i.get_isbn():
                return i
        return False

    def update_book(self, title, author, isbn, publication):
        for bk in Books.books_log:
            if bk.get_isbn() == isbn:
                bk.title = title
                bk.author = author
                bk.isbn = isbn
                bk.publication = publication
                return True
        return False

    def delete_book(self, isbn):
        for bk in Books.books_log:
            if isbn == bk.get_isbn():
                Books.books_log.remove(bk)
                return f"Book deleted successfully for ISBN: {isbn}"
        return f"Book not found for ISBN: {isbn}"

    def issue_book(self,isbn):
        for bk in Books.books_log:
            if bk.get_isbn() == isbn:
                Books.issue_books_log.append(bk)
                return "\nBook issued succeffully"

    def get_issue_book_by_isbn(isbn):
        for i in Books.issue_books_log:
            if isbn == i.get_isbn():
                return i
        return False

    def get_issue_books_log(self):
        return Books.issue_books_log

    def return_book(self,isbn):
        for bk in Books.issue_books_log:
            if bk.get_isbn() == isbn:
                Books.issue_books_log.remove(bk)
                return f"\nSuccessfully returned book of isbn, {isbn}"
            else:
                return f"\nBook not found"
        return f"\nBook not found"
        