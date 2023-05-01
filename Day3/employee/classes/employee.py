import sys
sys.path.append("D:/iti/backend/python/lab/Day3/employee")
from database.db_handler import *

class Employee:
    conn = db_handler.connect_to_database()
    all_employees = db_handler.show_all_employees(conn)


    # Constructor of Employee class
    def __init__(self, first_name, last_name, age, department, salary,managed_department=''):

        # Assign values to the instance attributes
        self.first_name = first_name
        self.last_name =  last_name
        self.age = age
        self.department= department
        self.salary = salary
        self.managed_department= managed_department

        # Insert new record in table employee in database
        conn = db_handler.connect_to_database()
        self.id =db_handler.insert_employee_record(conn,self)
        db_handler.close_database_connection(conn)

    def transfer_employee(employee_id, new_department):
        conn = db_handler.connect_to_database()
        db_handler.update_employee_record(conn,employee_id,new_department)
        db_handler.close_database_connection(conn)



    #get all employees from database
    @staticmethod
    def List_employees():
        conn = db_handler.connect_to_database()
        employees= db_handler.show_all_employees(conn)
        Employee.print_employees(employees)
        db_handler.close_database_connection(conn)


    # fire employee from database
    def fire_employee(employee_id):
        conn = db_handler.connect_to_database()
        db_handler.fire_employee_by_id(conn,employee_id)
        db_handler.close_database_connection(conn)
    

    def show(employee_id):
        conn = db_handler.connect_to_database()
        emp=db_handler.show_employee_by_id(conn,employee_id)
        Employee.print_employees(emp)
        db_handler.close_database_connection(conn)
    


    def print_employees(emp):
          table = PrettyTable()
          table.field_names = ["ID", "firstName","lastName", "AGE", "DEPARTMENT", "SALARY","managed_department"]
          for employee in emp:
            table.add_row(employee)
          print(table)

