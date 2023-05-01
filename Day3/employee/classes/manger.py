from  employee import Employee
from database.db_handler import *

class Manager(Employee):
    def __init__(self,first_name, last_name, age, department, salary,managed_department ):
        self.managed_department = managed_department
        super().__init__(first_name, last_name , age , department , salary ,managed_department )


    @staticmethod
    def show_manger(employee_id):
        conn = db_handler.connect_to_database()
        manger=db_handler.show_employee_by_id(conn,employee_id)
        Manager.print_manager(manger)
        db_handler.close_database_connection(conn)


    def print_manager(manager):
        table = PrettyTable()
        table.field_names = ["ID", "firstName", "lastName", "AGE", "DEPARTMENT", "SALARY", "managed_department"]
        for employee in manager:
            # Replace the salary value with "confidential"
            employee_with_confidential_salary = list(employee)
            salary_index = table.field_names.index("SALARY")
            employee_with_confidential_salary[salary_index] = "confidential"
            table.add_row(employee_with_confidential_salary)
        print(table)


