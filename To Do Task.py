import os
tasks = []
def add_task(task):
    tasks.append({"task": task, "completed": False})
def view_tasks():
    if not tasks:
        print("\n📭 No tasks yet.")
        return
    print("\n📋 Your To-Do List:")
    for idx, t in enumerate(tasks, 1):
        status = "✓" if t["completed"] else "✗"
        print(f"{idx}. [{status}] {t['task']}")
def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"✅ Removed: {removed['task']}")
    else:
        print("❌ Invalid task number.")
def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"🎉 Completed: {tasks[index]['task']}")
    else:
        print("❌ Invalid task number.")
def progress_bar():
    if not tasks:
        print("\n📊 Progress: 0% [░░░░░░░░░░]")
        return
    completed = sum(1 for t in tasks if t["completed"])
    percent = (completed / len(tasks)) * 100
    bar_length = 10
    filled = int(bar_length * completed / len(tasks))
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\n📊 Progress: {percent:.0f}% [{bar}] ({completed}/{len(tasks)} tasks done)")
def main():
    while True:
        print("\n" + "=" * 40)
        print("📝 TO-DO LIST APPLICATION")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Show progress")
        print("6. Exit")
        choice = input("Choose option (1-6): ").strip()
        if choice == "1":
            task_name = input("Enter task: ").strip()
            if task_name:
                add_task(task_name)
                print("✅ Task added.")
            else:
                print("❌ Task cannot be empty.")
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            if tasks:
                try:
                    idx = int(input("Enter task number to remove: ")) - 1
                    remove_task(idx)
                except ValueError:
                    print("❌ Invalid input.")
        elif choice == "4":
            view_tasks()
            if tasks:
                try:
                    idx = int(input("Enter task number to mark complete: ")) - 1
                    complete_task(idx)
                except ValueError:
                    print("❌ Invalid input.")
        elif choice == "5":
            progress_bar()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()