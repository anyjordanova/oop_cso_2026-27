from logging import currentframe

from people import Employee

if __name__ == "__main__":
    # put into code selection of job titles, even with exceptions
    # check for lowest paid person
    
    job_titles = ["Intern", "Short-term Intern", "Junior Manager", "Staff", "Senior Manager", "Manager", "Useless Position" ]
    employees = []
        
    for i in range(2):
        # Enter first name
        first_name = input(f"Enter first name of {i+1}. employee: ")
        
        # Enter last name
        last_name = input(f"Enter last name of {i+1}. employee: ")
        
        # Enter ID
        id = input(f"Enter Id of {i+1}. employee: ")
        
        # If user enters id that already exists, ask for a new id
        while any(emp.id == id for emp in employees): # using "any" command for inline loop
            print(f"Id {id} already exists. Please enter a new Id.")
            id = input(f"Enter Id of {i+1}. employee: ")
        
        # Salary enter
        salary = float(input(f"Enter salary of {i+1}. employee: "))
        
        # Enter job title from list
        print("Select job title from the following options:")
        for x, title in enumerate(job_titles):
            print(f"{x + 1}. {title}")
        
        # Save job title index
        job_title_index = int(input(f"Enter the number corresponding to the job title of {i+1}. employee: ")) - 1
        
        # Chech if index is valid
        while job_title_index < 0 or job_title_index >= len(job_titles):
            print("Invalid selection. Please select a valid job title number.")
            job_title_index = int(input(f"Enter the number corresponding to the job title of {i+1}. employee: ")) - 1
        
        # Get job title based on index
        job_title = job_titles[job_title_index]
        
        # create a new employee
        employee = Employee(id=id, first_name=first_name, last_name=last_name, salary=salary, job_title=job_title)
        employees.append(employee)
        
        # Print new employee
        print(f"Employee {i+1} details: {employee.display()}")
        
    # Find the employee with the lowest salary
    def find_lowest_net_pay(employees):
        lowest_salary = employees[0].calc_net_pay()
        index = -1
        for i in range(len(employees)):
            current = employees[i].calc_net_pay()
            if current < lowest_salary:
                lowest_salary = current
                index = i
        return index, lowest_salary
        
    # Find employee with highest bonus and display their details
    def find_highest_bonus(employees):
        highest_bonus = employees[0].calc_bonus()
        index = -1
        for i in range(len(employees)):
            current = employees[i].calc_bonus()
            if current > highest_bonus:
                highest_bonus = current
                index = i
        return index, highest_bonus
    
    # Print outcomes of the functions
    lowest_index, lowest_salary = find_lowest_net_pay(employees)
    print(f"Employee with the lowest net pay is: {employees[lowest_index].display()} with a net pay of {lowest_salary:.2f}")
    
    highest_index, highest_bonus = find_highest_bonus(employees)
    print(f"Employee with the highest bonus is: {employees[highest_index].display()} with a bonus of {highest_bonus:.2f}")
