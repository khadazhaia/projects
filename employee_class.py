from datetime import datetime
import datetime

'''
The system allows the business to store and manage employee data, and perform tasks related to employee management, such as adding and removing employees, updating employee information, searching for employees by name or department, and calculating total salary expenses.
'''
class Employee:
    
     def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: int):
         ''' intitalization, attributes, type hinting '''
         self.name = name
         self.job_title = job_title
         self.department = department
         self.salary = salary
         self.hire_year = hire_year

     def __str__(self):
         ''' return a string representation '''
         return f"{self.name} is a {self.job_title} in the {self.department} department who was hired in {self.hire_year} and makes {self.salary:.02f}"
    
     def years_worked(self):
         ''' return the total years this employee has worked here '''
         today = datetime.datetime.now()
         year = today.year
         return year - self.hire_year
    
 
     def total_expense(self):
         ''' calculate the total salary expense for this employee '''
         return self.salary * self.years_worked()
  
     def write_employees(self):
         ''' Write employee information to a text file '''
         f = open("employee_information.txt", "w")
         f.write(f'''{self.name} is a {self.job_title} in the {self.department} department who was hired in {self.hire_year} and makes {self.salary:.02f}''')
         f.close()
    
     ''' add accessor and mutator methods for each attribute so a user doesn't need to access them directly '''
     
     ''' Accessor method '''
     def get_name(self):
         return self.name
    
     def get_job_title(self):
         return self.job_title

     def get_department(self):
         return self.department

     def get_salary(self):
         return self.salary 

     def get_hire_year(self):
         return self.hire_year
     
     ''' Mutator method '''
     def set_name(self, new_name):
        self.name = new_name

     def set_job_title(self, new_job_title):
        self.job_title = new_job_title

     def set_department(self, new_department):
        self.department = new_department

     def set_salary(self, new_salary):
        self.salary = new_salary

     def set_hire_year(self, new_hire_year):
        self.hire_year = new_hire_year
   

employee1 = Employee("Zhaia", "Python Developer", "Engineering", 145000, 2020)
employee2 = Employee("Ally", "Software Engineer", "Engineering", 160000, 2018)
employee3 = Employee("Nas", "Data Scientist", "Data", 125000, 2023)
