import os

TASKS_FILE = "tasks.txt"

tasks = []

def display_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task[2] else "Incomplete"
            print(f"{i}. Title: {task[0]}\n   Description: {task[1]}\n   Status: {status}\n")

def add_task(title, description):
    tasks.append((title, description, False))
    print(f"Added task: {title}")

def mark_task(task_number, completed=True):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1] = (tasks[task_number - 1][0], tasks[task_number - 1][1], completed)
        print(f"Marked task {task_number} as {'Completed' if completed else 'Incomplete'}")
    else:
        print("Invalid task number.")

def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Removed task: {removed_task[0]}")
    else:
        print("Invalid task number.")

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task[0]},{task[1]},{task[2]}\n")
    print("Tasks saved successfully.")

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            for line in file:
                title, description, completed = line.strip().split(",")
                tasks.append((title, description, completed == "True"))
    except FileNotFoundError:
        print("No tasks found. Create a new task to get started.")

def main():
    load_tasks()
    while True:
        print("\nOptions:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Mark task as complete")
        print("4. Mark task as incomplete")
        print("5. Remove task")
        print("6. Save tasks")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_tasks()
        elif choice == "2":
            title = input("Enter the task title: ")
            description = input("Enter the task description: ")
            add_task(title, description)
        elif choice == "3":
            display_tasks()
            task_number = int(input("Enter the task number to mark as complete: "))
            mark_task(task_number, completed=True)
        elif choice == "4":
            display_tasks()
            task_number = int(input("Enter the task number to mark as incomplete: "))
            mark_task(task_number, completed=False)
        elif choice == "5":
            display_tasks()
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        elif choice == "6":
            save_tasks()
        elif choice == "7":
            save_tasks()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()