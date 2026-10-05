class Person:

    # Constructor
    def __init__(self, first_name="John", last_name="Doe", age=50, is_left=False):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.is_left = is_left
        
    # Method to display person's details (this is not part of assignment, but it's nice to have a getter method)
    def display_details(self):
        if self.is_left:
            print(f"Name: {self.first_name} {self.last_name}")
        # If right handed, displays in upper case
        else:
            print(f"Name: {self.first_name.upper()} {self.last_name.upper()}")
        print(f"Age: {self.age}")

class Employee:
    
    # Constructor
    def __init__(self, id, first_name=None, last_name=None, salary=None, job_title=None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.__salary = salary
        self.job_title = job_title
        
    def get_salary(self):
        return self.__salary
    
    def display(self):
        return f"Employee[id={self.id}, first_name={self.first_name}, last_name={self.last_name}, salary={self.__salary}]"
    
    def calc_net_pay(self):
        if self.__salary is None:
            return None
        else:
            tax = self.__salary * 0.42
            take_home_pay = self.__salary - tax
            monthly_take_home_pay = take_home_pay / 12
            return monthly_take_home_pay
    
    def calc_bonus(self):
        if "manager" in self.job_title:
            return self.__salary * 0.15
        elif "intern" in self.job_title:
            return self.__salary * 0.02
        else:
            return self.__salary * 0.06
        
    
        