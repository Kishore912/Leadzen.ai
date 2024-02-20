class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def delete_task(self, task_index):
        if task_index >= 0 and task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully!")
        else:
            print("Invalid task index!")

    def mark_completed(self, task_index):
        if task_index >= 0 and task_index < len(self.tasks):
            self.tasks[task_index] += " (Completed)"
            print("Task marked as completed!")
        else:
            print("Invalid task index!")

    def display_tasks(self):
        print("To-Do List:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")


def List():
    todo_list = ToDoList()
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "3":
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_completed(task_index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

List()
