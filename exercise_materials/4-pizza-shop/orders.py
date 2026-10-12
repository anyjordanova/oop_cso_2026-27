from itertools import count


class Pizza:
    # Static variable to hold valid sizes so it doesn't need to be redefined for each instance
    __sizes = ["Small", "Medium", "Large", "Extra-large"]
    toppings = ["Mushroom", "Pepperoni", "Green Peppers", "Olives", "Chives", "Bacon", "Pineapple", "Sausage", "Onions", "Spinach"]
    premium_toppings = ["Truffle Oil", "Prosciutto", "Artichoke Hearts", "Sun-dried Tomatoes", "Feta Cheese", "Goat Cheese", "Smoked Salmon", "Lobster", "Caviar"]
    
    def __init__(self, toppings: list, size:str="Medium"):    
        size = size.title()  # Normalize size input to title case
    
        # Validate size
        if size in Pizza.__sizes:
            self.__size = size
        else:
            raise ValueError(f"Invalid size: {size}. Valid sizes are: {Pizza.__sizes}")
        
        # Set correct text format for toppings
        toppings = [topping.title() for topping in toppings]
        
        # Validate toppings
        for topping in toppings:
            if topping not in Pizza.toppings and topping not in Pizza.premium_toppings:
                raise ValueError(f"Invalid topping: {topping}. Valid toppings are: {Pizza.toppings + Pizza.premium_toppings}")
            else:
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
    
    def add_topping(self, new_topping):
        # Set correct text format
        new_topping = new_topping.title()
        
        if new_topping in Pizza.toppings or new_topping in Pizza.premium_toppings:
            self.toppings.append(new_topping)
            return True
        else:
            raise ValueError(f"Invalid topping: {new_topping}. Valid toppings are: {Pizza.toppings + Pizza.premium_toppings}")
        
    def remove_topping(self, to_be_removed):
        # Correct format
        to_be_removed = to_be_removed.title()
        
        if to_be_removed in self.toppings:
            self.toppings.remove(to_be_removed)
            return True
        else:
            return False
        
if __name__  == "__main__":  
    pizza1 = Pizza(["pepperoni", "green peppers","mushroom", "Olives", "Chives"], "large")
    pizza1.display()
    print(pizza1.get_size())
    print(pizza1.set_size("small"))
    print(pizza1.set_size("personal"))
    print(pizza1.get_size())
    print(pizza1.get_num_toppings())
    print(pizza1.add_topping("goat cheese"))
    print(pizza1.remove_topping("pepperoni"))
    pizza1.display()


#this will raise a error
    try:
        pizza3 = Pizza(["bacon"], "Personal")
        pizza3.display()
    except ValueError as e:
        print(e)
        