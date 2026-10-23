
print("==== COURSE REGISTRATION SYSTEM ====")

name = input("Enter student name: ")

courses = [
    "Python Programming",
    "Engineering Mathematics",
    "Material Physics",
    "Engineering Graphics"
]

selected = []

while True:
    print("\n1. Show Courses")
    print("2. Register Course")
    print("3. View Courses")
    print("4. Registration Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for i, course in enumerate(courses, 1):
            print(i, ".", course)

    elif choice == "2":
        try:
            num = int(input("Enter course number: "))

            if 1 <= num <= len(courses):
                course = courses[num - 1]

                if course not in selected:
                    selected.append(course)
                    print("Course registered!")
                else:
                    print("Already registered!")
            else:
                print("Invalid course number!")

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "3":
        print("\nStudent:", name)
        print("Registered Courses:", selected)

    elif choice == "4":
        print("\n==== REGISTRATION SUMMARY ====")
        print("Student Name:", name)
        print("Total Available Courses:", len(courses))
        print("Total Registered Courses:", len(selected))

        if selected:
            print("Registered Courses:")
            for course in selected:
                print("-", course)
        else:
            print("No courses registered yet.")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid choice!")
