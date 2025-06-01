todo_list = []

while True:
    task = input("Enter a task (or 'done' to finish): ")
    if task.lower() == 'done':
        break
    todo_list.append(task)

print("\nYour To-Do List:")
for i, task in enumerate(todo_list, 1):
    print(f"{i}. {task}")
