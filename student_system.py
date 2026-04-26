students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        students[name] = marks
        print("Student added successfully")

    elif choice == "2":
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in students:
            del students[name]
            print("Deleted successfully")
        else:
            print("Student not found")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
