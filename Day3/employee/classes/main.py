from  employee import Employee
from  manger import Manager
import sys


class App:


    def run(self):
        while True:
            # print the menu
            print("Menu:")
            print("1. Add new employee")
            print("2. List employees")
            print("3. Fire employee")
            print("4. update employee department")
            print("5. show specific employee")
            print("6. show specific manger")
            print("7. Quit program")

            # get user input
            choice = input("Enter your choice: ")

            # check if the choice is valid
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.show_all_emp()
            elif choice == "3":
                self.fire()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.show_emp_by_id()
            elif choice == "6":
                self.show_manger_by_id()
            elif choice == "7":
                self.quit_program()
            else:
                print("Invalid choice. Please try again.")
    def add_employee(self):
        print("Please insert data:")
        first_name = input("Name: ")
        last_name = input("Last name: ")
        age = int(input("Age: "))
        department = input("Department: ")
        salary = float(input("Salary: "))
        # ask if the employee is a manager
        if input("Is the employee a manager? (y/n): ").lower() == "y":
            managed_department = input("Managed department: ")
            Manager(first_name, last_name, age, department, salary, managed_department)
        else:
            Employee(first_name, last_name, age, department, salary , managed_department='')

    def show_all_emp(self):
        Employee.List_employees()

    def fire(self):
        employee_id = input("employee ID : ")
        Employee.fire_employee([int(employee_id)])

    def update_employee(self):
        new_department = input("new department : ")
        employee_id =int(input("employee ID : "))
        Employee.transfer_employee(employee_id,new_department)

    def show_emp_by_id(self):
        employee_id = input("employee ID : ")
        Employee.show([int(employee_id)])

    def show_manger_by_id(self):
        employee_id = input("manger ID : ")
        Manager.show_manger([int(employee_id)])

    def quit_program(self):
        print("Thank you for using our program... plz come again ^_^")
        sys.exit()

app = App()
app.run()