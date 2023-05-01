import mysql.connector
from mysql.connector import connect, Error
from prettytable import PrettyTable

class db_handler:
    conn={}
    def connect_to_database():
        try:
            connection = connect(
                host="localhost",
                user="root",
                password="",
                database='python_lab_2'
            )
            return connection
        except Error as e:
            print("Error connecting to database")
            print(e)

    def close_database_connection(connection):
        try:
            connection.close()
            print("Database connection closed")
        except Error as e:
            print("Error closing database connection")
            print(e)

    def insert_employee_record(connection, self ):
        try:
            my_cursor = connection.cursor()
            query = "INSERT INTO employees (first_name, last_name, age, department, salary, managed_department) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (self.first_name, self.last_name,  self.age, self.department, self.salary, self.managed_department)
            my_cursor.execute(query, values)
            connection.commit()
            employee_id =  my_cursor.lastrowid
            print("Record inserted successfully")
        except Error as e:
            print("Error inserting employee record")
            print(e)
        return employee_id


    def update_employee_record(connection,id,department):
        try:
            my_cursor = connection.cursor()
            query = "UPDATE employees SET  department = %s WHERE id = %s"
            values = (department,id)
            my_cursor.execute(query, values)
            connection.commit()
            print("Record updated successfully")
        except Error as e:
            print("Error updating employee record")
            print(e)

    def fire_employee_by_id(connection,id):
        try:
            my_cursor = connection.cursor()
            query = "DELETE FROM employees WHERE id = %s"
            values = (id)
            my_cursor.execute(query, values)
            connection.commit()
            print("Record deleted successfully")
        except Error as e:
            print("Error deleting employee record")
            print(e)




    def show_all_employees(connection):
        try:
            my_cursor = connection.cursor()
            query = "SELECT * FROM employees"
            my_cursor.execute(query)
            result = my_cursor.fetchall()
            return result
        except Error as e:
            print("Error showing all employees")
            print(e)


    def show_employee_by_id(connection,id):
        try:
            my_cursor = connection.cursor()
            query = "SELECT * FROM employees WHERE id = %s"
            values = (id)
            my_cursor.execute(query, values)
            result = my_cursor.fetchall()
            return result
        except Error as e:
            print("Error showing employee")
            print(e)

