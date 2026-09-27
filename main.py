from student import add_student,view_students,update_student,delete_student,search_student

while True:
    print("\n====Student Management System====")

    print("1. Add student")
    print("2. View students")
    print("3. Update student")
    print("4. Delete student")
    print("5. Search student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()

    elif choice=='2':
        view_students()

    elif choice == '3':
        update_student()

    elif choice == '4':
        delete_student()

    elif choice == '5':
        search_student()

    elif choice == '6':
        print("Thank you")
        break

    else:
        print("Invalid choice. Please try again.")

    

