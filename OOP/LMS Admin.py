class Admin:
    admin_list = list()
    def __init__(self,admin_email,admin_pw) -> None:
        self.email = admin_email
        self.pw = admin_pw


    def add_new_admin(self):
        Admin.admin_list.append(self)
        print("Admin added")
    
    def display_admins(self):
        for ad in Admin.admin_list:
            print(ad)


for i in range(3):
    email = input("Enter email: ")
    # pw = input("Enter pw: ")

    admin = email
    Admin.admin_list.append(admin)
    print(admin)

Admin.display_admins(Admin)





