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
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for i, course in enumerate(courses, 1):
            print(i, ".", course)

    elif choice == "2":
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

    elif choice == "3":
        print("\nStudent:", name)
        print("Courses:", selected)

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid choice!")