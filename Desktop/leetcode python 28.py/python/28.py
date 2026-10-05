# ==========================================
# STUDENT MANAGEMENT SYSTEM
# ==========================================

students = []


# ------------------------------------------
# 1. Add Student
# ------------------------------------------

def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")


# ------------------------------------------
# 2. Display Students
# ------------------------------------------

def display_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No students found.")
        return

    for i, student in enumerate(students, start=1):
        print(
            f"{i}. Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Marks: {student['marks']}"
        )


# ------------------------------------------
# 3. Find Student
# ------------------------------------------

def find_student():
    print("\n--- Find Student ---")

    name = input("Enter student name: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])

            found = True
            break

    if not found:
        print("Student not found.")


# ------------------------------------------
# 4. Calculate Grade
# ------------------------------------------

def calculate_grade():
    print("\n--- Student Grades ---")

    if len(students) == 0:
        print("No students available.")
        return

    for student in students:

        marks = student["marks"]

        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"

        print(
            f"{student['name']} -> "
            f"Marks: {marks}, Grade: {grade}"
        )


# ------------------------------------------
# 5. Find Top Student
# ------------------------------------------

def top_student():
    print("\n--- Top Student ---")

    if len(students) == 0:
        print("No students available.")
        return

    top = students[0]

    for student in students:
        if student["marks"] > top["marks"]:
            top = student

    print("Top Student:", top["name"])
    print("Marks:", top["marks"])


# ------------------------------------------
# 6. Calculate Average
# ------------------------------------------

def calculate_average():
    print("\n--- Class Average ---")

    if len(students) == 0:
        print("No students available.")
        return

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    print("Class Average:", average)


# ------------------------------------------
# 7. Sort Students
# ------------------------------------------

def sort_students():
    print("\n--- Students Sorted by Marks ---")

    if len(students) == 0:
        print("No students available.")
        return

    sorted_students = sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True
    )

    for student in sorted_students:
        print(
            student["name"],
            "-",
            student["marks"]
        )


# ------------------------------------------
# 8. Delete Student
# ------------------------------------------

def delete_student():
    print("\n--- Delete Student ---")

    name = input("Enter student name: ")

    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            print("Student deleted successfully!")

            return

    print("Student not found.")


# ------------------------------------------
# 9. Statistics
# ------------------------------------------

def statistics():
    print("\n--- Class Statistics ---")

    if len(students) == 0:
        print("No students available.")
        return

    highest = students[0]["marks"]
    lowest = students[0]["marks"]

    pass_count = 0
    fail_count = 0

    for student in students:

        marks = student["marks"]

        if marks > highest:
            highest = marks

        if marks < lowest:
            lowest = marks

        if marks >= 40:
            pass_count += 1
        else:
            fail_count += 1

    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Passed Students:", pass_count)
    print("Failed Students:", fail_count)


# ------------------------------------------
# Main Menu
# ------------------------------------------

while True:

    print("\n================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Find Student")
    print("4. Calculate Grades")
    print("5. Find Top Student")
    print("6. Calculate Class Average")
    print("7. Sort Students")
    print("8. Delete Student")
    print("9. Class Statistics")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        find_student()

    elif choice == "4":
        calculate_grade()

    elif choice == "5":
        top_student()

    elif choice == "6":
        calculate_average()

    elif choice == "7":
        sort_students()

    elif choice == "8":
        delete_student()

    elif choice == "9":
        statistics()

    elif choice == "10":
        print("\nThank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")