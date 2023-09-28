from sqlalchemy.orm import sessionmaker
from models import TodoList, engine

Session = sessionmaker(bind=engine)

# Function to add a task to the todo list


def add_task(task):
    session = Session()
    new_task = TodoList(task=task)
    session.add(new_task)
    session.commit()
    session.close()
    print('Task added successfully.')

# Function to mark a task as completed


def complete_task(task_id):
    session = Session()
    task = session.query(TodoList).filter_by(id=task_id).first()
    if task:
        task.completed = True
        session.commit()
        print('Task marked as completed.')
    else:
        print('Task not found.')

# Function to delete completed tasks


def delete_completed_tasks():
    session = Session()
    completed_tasks = session.query(TodoList).filter_by(completed=True).all()
    if not completed_tasks:
        print('No completed tasks found.')
    else:
        for task in completed_tasks:
            session.delete(task)
        session.commit()
        print('Completed tasks deleted successfully.')
    session.close()

# Function to display all tasks in the todo list


def display_tasks():
    session = Session()
    tasks = session.query(TodoList).all()
    session.close()
    if not tasks:
        print('No tasks found.')
    else:
        for task in tasks:
            status = 'Completed' if task.completed else 'Incomplete'
            print(f'Task ID: {task.id}\tTask: {task.task}\tStatus: {status}')
