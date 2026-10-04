import math

from shapes import Rectangle
import random

def find_greatest_area(rect_list):
    max_area = -1
    biggest = None

    for rect in rect_list:
        if rect.calc_area() > max_area:
            max_area = rect.calc_area()
            biggest = rect

    return biggest

def find_min_width(rect_list):
    if not rect_list:
        return None

    min_width = rect_list[0].width
    smallest = None

    for rect in rect_list:
        if rect.width < min_width:
            min_width = rect.width
            smallest = rect

    return smallest


if __name__ == "__main__":
    rectangles = []

    for i in range(5):
        # Create new default Rectangle
        
        # Take in details for new Rectangle
        length = float(input(f"Enter length of rectangle {(i+1)}: "))
        width = float(input(f"Enter width of rectangle {(i + 1)}: "))

        # If number is odd, user can select colour, otherwise default colour is used
        if random.randint(1,10) % 2 == 0:
            colour = input(f"Enter colour of rectangle {(i + 1)}: ")
            rect = Rectangle(length, width, colour)
        else:
            rect = Rectangle(length, width)        

        # Save rectangle in the list
        rectangles.append(rect)

    max_rect = find_greatest_area(rectangles)
    if max_rect is not None:
        print("Rectangle with greatest area:")
        max_rect.display()

    min_rect = find_min_width(rectangles)
    if min_rect is not None:
        print("Rectangle with smallest width:")
        min_rect.display()