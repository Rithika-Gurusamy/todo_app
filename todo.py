
import json

class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True


def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)


def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []


def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\nYour Tasks:")
    print("-" * 40)
    for idx, task in enumerate(tasks):
        status = "✓ Done" if task.completed else "✗ Not Done"
        print(f"{idx + 1}. {task.title} [{task.category}]")
        print(f"   {task.description}")
        print(f"   Status: {status}")
        print("-" * 40)


def main():
    tasks = load_tasks()

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")
        print("=============================")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            print("\n--- Add a New Task ---")
            title = input("Title: ")
            desc = input("Description: ")
            category = input("Category (Work/Personal/Urgent): ")
            tasks.append(Task(title, desc, category))
            print("✅ Task added successfully!")

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            display_tasks(tasks)
            idx = input("Enter task number to mark complete: ")
            if idx.isdigit() and 0 < int(idx) <= len(tasks):
                tasks[int(idx) - 1].mark_completed()
                print("✅ Task marked as completed!")
            else:
                print("❌ Invalid task number.")

        elif choice == '4':
            display_tasks(tasks)
            idx = input("Enter task number to edit: ")
            if idx.isdigit() and 0 < int(idx) <= len(tasks):
                task = tasks[int(idx) - 1]
                print("\nLeave blank to keep existing value.")
                new_title = input(f"New Title [{task.title}]: ") or task.title
                new_desc = input(f"New Description [{task.description}]: ") or task.description
                new_cat = input(f"New Category [{task.category}]: ") or task.category

                task.title = new_title
                task.description = new_desc
                task.category = new_cat
                print("✅ Task updated!")
            else:
                print("❌ Invalid task number.")

        elif choice == '5':
            display_tasks(tasks)
            idx = input("Enter task number to delete: ")
            if idx.isdigit() and 0 < int(idx) <= len(tasks):
                deleted = tasks.pop(int(idx) - 1)
                print(f"🗑️ Task '{deleted.title}' deleted.")
            else:
                print("❌ Invalid task number.")

        elif choice == '6':
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
