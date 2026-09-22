basket = [
    {"name": "Yogurt", "price": 1.79, "quantity": 4},
    {"name": "Bread", "price": 1.80, "quantity": 1},
    {"name": "Milk", "price": 1.59, "quantity": 2}
]

expensive_basket = [
    {"name": "Cheerios", "price": 7.80, "quantity": 3},
    {"name": "Coke Zero", "price": 12.00, "quantity": 4},
]

#C1 Calculate total price of dic

def calculate_total_price(basket_list):
    total_price = 0
    for item in basket_list:
        total_price += (item["price"] * item["quantity"])
        
    # If total price is more than €50, it will give 10% discount
    if total_price >= 50:
        total_price *= 0.9
        
    return total_price
         
print(f"Total value of basket is: {calculate_total_price(basket)}")
print(f"Total value of expensive basket is: {calculate_total_price(expensive_basket)}")

# C2 Print invoice for basket

# Gets item form basket list and calculates total price for current item
def calculate_total_of_one_item(item):
        return item["price"] * item["quantity"]

def print_receipt(basket_list):
    for item in basket_list:
        # Print the structure + call function to calculate total price of 1 item
        print(f"{item["name"]}  {item["quantity"]} x €{item["price"]:.2f}  €{calculate_total_of_one_item(item):.2f}")
    print("-"*25)
    print(f"Total:           €{calculate_total_price(basket_list):.2f}")
    
# call function to print basket
print_receipt(basket)

# c3 find item in the basket
searched_item = input("What item do you want to search??")

def find_item(basket_list, item):
    for x in basket_list:
        # If match is find, print info and stops - returns
        if x["name"] == item:
            print(f"Name: {x["name"]}, Price: {x["price"]}, Quantity: {x["quantity"]}")
            return
    # No match found -> prints "error message"
    print("Item not in the list")
    
find_item(basket, searched_item)
    
# c4 Change quantity in the basket
item = input("Enter Item name: ")
quantity = input("Enter new quantity: ")

def change_quantity(basket_list, item_name, new_quantity):
    for x in basket_list:
        # If match is find, print info and stops - returns
        if x["name"] == item_name:
            if new_quantity.isnumeric():
                if int(new_quantity) >= 0:
                    x["quantity"] = int(new_quantity)
                    return "Quantity changed to " + new_quantity
                else:
                    return "Quantity less than 0."
            else:
                return "Not a Number"
            
    # If no item found
    return "Item with this name does not exist"

print(change_quantity(basket, item, quantity))

# c5 calculate discount
