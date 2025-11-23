from staff import Staffs

class AppMenu:
    def __init__(self):
        self.staff = Staffs()

    def display(self):
        while True:
            print("\n ==Menu ==")
            print("1. Create Staff")
            print("2. Read All Staffs")
            print("3. Update Staff")
            print("4. Delete Staff")
            print("5. Exit")

            choice = input("Choose what you want to do :")

            if choice == "1":
                name = input("Enter your name : ")
                email = input("Enter your email : ")
                self.staff.create(name,email)

            elif choice == "2":
                self.staff.readall()

            elif choice == "3":
                userid = input("Enter ID to update : ")
                newname = input("Enter new name : ")
                newemail = input("Enter new email : ")
                self.staff.update(userid,newname,newemail)

            elif choice == "4":
                deleteid = input("Enter ID to delete : ")
                self.staff.delete(deleteid)
                
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid Service Number! Please choose again !")

            