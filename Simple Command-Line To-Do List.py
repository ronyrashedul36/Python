tasks = []

print("--- Welcome to your To-Do List ---")

while True:
    print("\nPlease choose an option: ")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Exit")

    choice = input("Enter your choice (1,2, or 3): ")

    if choice == "1":
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print(f"Task {new_task} added successfully!")
    elif choice == "2":
        print("\n--- Your Tasks ---")
        if not tasks:
            print("You have no tasks yet.")
        else:
            for index, task in enumerate(tasks, start = 1):
                print(f"{index}.{task}")
    elif choice == "3":
        print("Thank you for using the To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")