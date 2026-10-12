from itertools import count


class Pizza:
    # Static variable to hold valid sizes so it doesn't need to be redefined for each instance
    __sizes = ["Small", "Medium", "Large", "Extra-large"]
    toppings = list
    
    def __init__(self, toppings: list, size:str="Medium"):    
        size = size.title()  # Normalize size input to title case

        # Validate size
        if size in Pizza.__sizes:
            self.__size = size
        else:
            raise ValueError(f"Invalid size: {size}. Valid sizes are: {Pizza.__sizes}")
        self.toppings = toppings
        
    def display(self):
         print(f"{self.__size}_Pizza with {', '.join(self.toppings)} toppings")

    def get_size(self):
        return self.__size
    
    def set_size(self, new_size):
        # Set correct text format
        new_size = new_size.title()
        # Validate if new size in the list
        if new_size in Pizza.__sizes:
            self.__size = new_size
            return True
        
        return False
    
    def get_num_toppings(self):
        return len(self.toppings)
    
if __name__  == "__main__":  
    pizza1 = Pizza(["pepperoni", "green peppers","mushroom", "Olives", "Chives"], "large")
    pizza1.display()
    print(pizza1.get_size())
    print(pizza1.set_size("small"))
    print(pizza1.set_size("personal"))
    print(pizza1.get_size())
    print(pizza1.get_num_toppings())


#this will raise a error
    try:
        pizza3 = Pizza(["bacon"], "Personal")
        pizza3.display()
    except ValueError as e:
        print(e)
        