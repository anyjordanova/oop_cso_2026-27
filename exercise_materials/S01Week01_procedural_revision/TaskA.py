# Student Average Marks

students = [
    {"name": "Annie", "average_mark": 55},
    {"name": "Aine", "average_mark": 39},
    {"name": "Mira", "average_mark": 66},
    {"name": "Dan", "average_mark": 47}
]

# A1 Access data
for student in students:
    print(student["name"], student["average_mark"])
    
print(students[-1]["average_mark"])

# A2 Selection of data
for student in students:
    if student["average_mark"] >= 50: print(student["name"])
        
# A3 calculation of avg mark
highest_avg = float(students[0]["average_mark"])
student_name = ""

for student in students:
    if float(student["average_mark"]) >= highest_avg: 
        highest_avg = float(student["average_mark"])
        student_name = student["name"]

print(f"{student_name} has the highest average: {highest_avg}")
        

