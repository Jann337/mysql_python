from crud import add_task, complete_task, delete_completed_tasks, display_tasks

# Prompt the user to add tasks until they are done
while True:
    task = input('Enter a task to add (or "done" to finish): ')
    if task.lower() == 'done':
        break
    add_task(task)

# Display all tasks
display_tasks()

# Prompt the user to enter the task ID to complete
task_id = (input('Enter the task ID to complete: '))

# Mark the task as completed
complete_task(task_id)

# Display all tasks again to see the updated status
display_tasks()

# Prompt the user to choose whether to delete completed tasks
choice = input('Do you want to delete completed tasks? (yes/no): ')
if choice.lower() == 'yes':
    delete_completed_tasks()

# Display all tasks after deleting completed tasks
display_tasks()
