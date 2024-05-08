
def grades():
    people = [
        {"name": "Alice", "age": 25, "grade": 85},
        {"name": "Bob", "age": 30, "grade": 78},
        {"name": "Charlie", "age": 22, "grade": 92},
        {"name": "David", "age": 28, "grade": 80},
        {"name": "Eve", "age": 26, "grade": 88}
    ]

    # 1 print name - age - grade
    for student in people:
        #print(student["name"] + " - " + str(student["age"]) + " - " + str(student["grade"]))
        
        # f string example
        print(f"{student['name']} - {student['age']} - {student['grade']}")
    
    print("-" * 25) # python only language that will allow strings and numbers to be (+, -, *, /)

    # 2 print the grade for David
    for student in people:
        if student["name"] == "David":
            print(f"The grade for David is: {student['grade']}")
    
    print("-" * 25)
    
    # 3 print the name and age of students with grades over 80
    for student in people:
        if student["grade"] > 80:
            print(f"{student['name']} {student['age']}")


# function calls
grades()