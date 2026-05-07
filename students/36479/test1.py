students = [
    {"name": "Alex", "age": 21, "major": "CS"},
    {"name": "John", "age": 22, "major": "Math"},
    {"name": "Emma", "age": 20, "major": "Physics"},
    {"name": "Liam", "age": 23, "major": "Engineering"}
]

# Access examples
print(students[0]["name"])  # Alex
print(students[1]["major"])  # Math

# Loop through all students
for student in students:
    print(student["name"], student["age"], student["major"])
