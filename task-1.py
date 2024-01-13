import json
from datetime import datetime

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task['title']} - {task['date']}")

def add_task(title):
    tasks = load_tasks()
    new_task = {"title": title, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully.")

def remove_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' removed successfully.")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nOptions:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            tasks = load_tasks()
            display_tasks(tasks)
        elif choice == "2":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "3":
            index = int(input("Enter the index of the task to remove: "))
            remove_task(index)
        elif choice == "4":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
