#To-Do List (Console App)
#Store tasks in a text file (open, read, write).
#Add features: mark complete, delete, view pending

import os
TODO_FILE = 'todo.txt'
DONE_FILE = 'done.txt'  
ARCHIVE_FILE = 'archive.txt'
MAX_TASKS = 100
PENDING_FILE = 'pending.txt'
ARCHIVE_LIMIT = 50
PENDING_LIMIT = 50
def load_tasks(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')     
def add_task(task):
    tasks = load_tasks(TODO_FILE)
    if len(tasks) >= MAX_TASKS:
        print("Task limit reached. Please complete or delete some tasks.")
        return
    tasks.append(task)
    save_tasks(TODO_FILE, tasks)
    print(f"Task added: {task}")
def view_tasks():
    tasks = load_tasks(TODO_FILE)
    if not tasks:
        print("No tasks found.")
        return
    print("To-Do List:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")
def mark_complete(task_number):
    tasks = load_tasks(TODO_FILE)
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return
    task = tasks.pop(task_number - 1)
    save_tasks(TODO_FILE, tasks)
    done_tasks = load_tasks(DONE_FILE)
    done_tasks.append(task)
    save_tasks(DONE_FILE, done_tasks)
    print(f"Task marked as complete: {task}")
    # Archive if done tasks exceed limit
    if len(done_tasks) > ARCHIVE_LIMIT:
        archive_tasks = done_tasks[:-ARCHIVE_LIMIT]
        done_tasks = done_tasks[-ARCHIVE_LIMIT:]
        save_tasks(DONE_FILE, done_tasks)
        archive = load_tasks(ARCHIVE_FILE)
        archive.extend(archive_tasks)
        save_tasks(ARCHIVE_FILE, archive)
        print(f"Archived {len(archive_tasks)} completed tasks.")
    # Maintain pending tasks
    pending_tasks = load_tasks(PENDING_FILE)    
    pending_tasks.append(task)
    if len(pending_tasks) > PENDING_LIMIT:
        pending_tasks = pending_tasks[-PENDING_LIMIT:]
    save_tasks(PENDING_FILE, pending_tasks)
def delete_task(task_number):
    tasks = load_tasks(TODO_FILE)
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return
    task = tasks.pop(task_number - 1)
    save_tasks(TODO_FILE, tasks)
    print(f"Task deleted: {task}")
def view_pending():
    pending_tasks = load_tasks(PENDING_FILE)
    if not pending_tasks:
        print("No pending tasks found.")
        return
    print("Pending Tasks:")
    for idx, task in enumerate(pending_tasks, 1):
        print(f"{idx}. {task}")
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. View Pending Tasks")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == '1':
            task = input("Enter the task: ").strip()
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to mark as complete: ").strip())
                mark_complete(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to delete: ").strip())
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            view_pending()
        elif choice == '6':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()  
# Run the program   

