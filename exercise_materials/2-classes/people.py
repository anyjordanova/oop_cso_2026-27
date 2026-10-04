class Person:
#     first_name = "Joe"
#     last_name = "Bloggs"
#     age = 25
#     is_left = False
    
    # Constructor
    def __init__(self, first_name="John", last_name="Doe", age=50, is_left=FalseP):
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
