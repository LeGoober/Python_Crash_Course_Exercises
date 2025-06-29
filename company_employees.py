"""
This program is about creating a Python program that 
will fulfill the conditions of the assignment brief of Creating an application
that has all the functionalities of the bried
"""
#Creating the base class for the program Employee
class Employee:
    def __init__(self, emp_name, emp_hrs_per_week = 36.5, emp_salary = 45000, emp_leave_days = 15):
        self.emp_name = emp_name
        self.emp_hrs_per_week = emp_hrs_per_week
        self.emp_salary = emp_salary
        self.emp_leave_days = emp_leave_days
        #Setting all the necessary functionalities of the Application
        def toString():
            return print("Employee Details [ Emp_Name:" + emp_name + ", Emp_Hours_Per_Week: " + emp_hrs_per_week + ", Emp_Salary: R" + emp_salary + ", Emp_Leave_Days: " + emp_leave_days)
        def setName(emp_name):
            emp_name = emp_name
        def getName():
            return emp_name
        def getSalary():
            return emp_salary
        def getHours():
            return emp_hrs_per_week
        def empLeaveApplication(emp_name):
            return print("Employee: " + emp_name + " has requested leave.")
        def empWork(emp_name):
            return print(emp_name + " is doing their job.")

class Manager(Employee):
    def __init__(self, emp_name, emp_hrs_per_week,emp_salary= 65000, emp_leave_days=18):
        super().__init__(emp_name, emp_hrs_per_week ,emp_salary, emp_leave_days)
        def emp_leave_application(emp_name):
            return print("The Manager: " + emp_name + " has requested leave.")
        def emp_work(emp_name):
            return print("The Employee: " + emp_name + " is a Manager at the company.")

class Secretary(Employee):
    def __init__(self, emp_name, emp_hrs_per_week = 40, emp_salary= 45000, emp_leave_days = 15):
        super().__init__(emp_name, emp_hrs_per_week, emp_salary, emp_leave_days)
        def empWork(emp_name):
            return print("The Employee: " + emp_name + " is a Secretary at the company.") 

#Creating a List to store all the different kinds of Employees        
Employee_List = [
        Employee("John", 38, 48000, 16),
        Employee("David", 36, 46000, 15),
        Employee("Tom", 36, 45000, 15),
        Employee("James", 36, 47000, 16)

]
Manager_List = [
        Manager("Sarah", 40, 65000, 18),
        Manager("Michael", 37, 67000, 18),
        Manager("Laura", 38, 66000, 18),

]
Secretary_List = [
        Secretary("Emily", 35, 40000, 12),
        Secretary("Anna", 34, 42000, 14),
        Secretary("Sam", 40, 43000, 14),

]
total_salary = 0
max_employees = 20

user_input = int(input("Welcome to the Employee Management System" 
      +" --------------------------------------"
      + "What would you like to do within our application:"
      +"\n1. Add a New Employee to The System;" 
      +"\n2. See what Employees are in the System"
      +"\n3. Place a Leave Application"
      +"\n4. Display the Average Salary"
      +"\n5. Display the Leave Costs"
      +"\n6. Exit the Application"
      +"\nEnter your input:"))
print("--------------------------------------")

while True:
    if(user_input == 1):
        if len(Employee_List or Secretary_List or Manager_List) >= max_employees:
            print("Maximum number of Employees in the List")
            continue
        user_input_2 = int("Enter the type of Employee you'd like to add into our List"
                           +"\n1. General Employee,"
                           +"\2. Manager,"
                           +"\n3. Secretary")
        if(user_input_2 == 1):
            user_name = str(input("Enter the Employee's Name: "))
            employee = Employee(user_name)
            Employee_List.append(employee)
        elif(user_input_2 == 2):
            user_name = str(input("Enter the Employee's Name: "))
            manager = Manager(user_name)
            Manager_List.append(manager)
        elif(user_input_2 == 3):
            user_name = str(input("Enter the Employee's Name: "))
            secretary = Secretary(user_name)
            Secretary_List.append(secretary)
    elif(user_input == 2):
        print("The list of General Employees in our System")
        for employees in Employee_List:
            print(Employee_List)
        print("-------------------------------------------")
        print("The list of Managers in our System")
        for managers in Manager_List:
            print(Manager_List)
        print("-------------------------------------------")
        print("The list of Secretaries in our System")
        for secretaries in Secretary_List:
            print(Secretary_List)
    elif(user_input == 3):
        user_input_3 = int(input("What kind of Employee type are you:"
              +"\n1. General Employee"
              +"\n2. Manager"
              +"\n3. Secretary"))
    elif(user_input == 4):
        total_salary = sum(employee.emp_salary for employee in Employee_List)
        average_salary = total_salary / len(Employee_List)
        print(f"\n The Average Salary of All Employee is: R{average_salary:.2f}")
    elif(user_input == 6):
        break