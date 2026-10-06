class Pizza:
    sizes = ["Small", "Medium", "Large", "Extra-large"]
    
    # Sizes: Small medium large Extra-large
    def __init__(self, toppings: list, size:str="Medium"):    
        # Validate size
        if size in Pizza.sizes:
            self.__size = size
        else:
            raise ValueError(f"Invalid size: {size}. Valid sizes are: {Pizza.sizes}")
        self.toppings = toppings
        
    