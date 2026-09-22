# More Complex Students
from functools import total_ordering, cache

students = [
 {"name": "Evan", "marks": [65, 72, 81]},
 {"name": "Caleb", "marks": [45, 51, 48]},
 {"name": "Angelo", "marks": [82, 77, 91]},
 {"name": "Dorothy", "marks": [55, 63, 59]}
]

# B1 Calculating avg
def calc_average(marks):
    total_score = sum(marks)
    total_avg = total_score / len(marks)
    return total_avg

print(calc_average([60,70,80]))

# B2 Processing data with functions
for student in students:
    print(f"{student["name"]}, average mark: {calc_average(student["marks"]):.1f}")

print(calc_average(students[1]["marks"]))

# B3 Printing nested selected data
for student in students:
    if calc_average(student["marks"]) >= 50: print(student["name"])

# B4 Amending nested data
name = input("Name of student you want to add mark to: ")
mark = float(input(f"What mark do you want to give to {name}?"))

# Find dictionary based on name inputed by user
def find_index(name):
    for student in students:
        if student["name"] == name:
            return student
    return ""
  
# Add mark to list
def add_mark(student_dict, new_mark):
    student_dict["marks"].append(new_mark)

# Run function to add mark
add_mark(find_index(name), mark)

#  Prints marks
print(find_index(name)["marks"])


    
