
students = []

def menu():
    print("\nSTUDENT RECORD SYSTEM")
    print(f"Total Students: {len(students)}")
    print("1. Add student")
    print("2. View Studnents")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Calculate Average")
    print("6. Exit")

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    students.append({"name": name, "grade": grade})
    print(f"Student {name} added successfully.")

def view_students():
    if not students:
        print("No students found.")
    else: 
        print("\nSTUDENT LIST")
        for student in students:
            print(f"Name: {student['name']}, Grade: {student['grade']}")

def search_student():
    search_name = input("Enter student name to search: ")
    found = False
    for student in students:
        if student["name"].lower() == search_name.lower():
            print(f"Name: {student['name']}, Grade: {student['grade']}")
            found = True 
            break
    if not found: 
        print(f"Student {search_name} not found.")

def delete_student():
    delete_name = input("Enter student name to delete: ")
    for student in students:
        if student["name"].lower() == delete_name.lower():
            students.remove(student)
            print(f"Student {delete_name} deleted successfully.")
            return
    print(f"Student {delete_name} not found.")

def calculate_average():
    if not students:
        print("No students found.")
    else:
        total_grade = sum(student["grade"] for student in students)
        average_grade = total_grade / len(students)
        print(f"Average grade of students: {average_grade: .2f}")


def main():
    while True:
        menu()
        choice = input("Enter you choice (1 - 6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            calculate_average()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()