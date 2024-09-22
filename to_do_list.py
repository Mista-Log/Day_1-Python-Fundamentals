




def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")



def mark_complete(tasks):
    task_index = int(input("Enter the index of the task to mark complete: "))
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        print("Task marked complete!")
    else:
        print("Invalid index.")





def view_tasks(tasks):
    print("Remaining Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")





def main():
    tasks = []
    while True:
        print("To-Do List Game")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            mark_complete(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

            