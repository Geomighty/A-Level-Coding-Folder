# Menu
print("""
      1. Add a task
      2. Display task lists
      3. Check the next task
      4. Mark task as complete
      5. Exit""")
option = int(input("Enter the number of the operation you want to perform."))

task_list = []
completed_task = []

def add_task(a):
    task_list.append(a)
    if a == "no":
        task_list.pop(len(task_list)-1)


def display_task_list():
    print("your tasks to complete are")
    for i in range(len(task_list)):
        print(f"{task_list[i]}")


def next_task():
    print(f"{task_list[0]}")


def mark_task_complete():
    task = str(input("Enter the task you want to mark completed: "))
    task_index = task_list.index(task)
    completed_task.append(task_index)
    task_list.pop(task_index)

while option != 5:
    
    if option == 1:
        new_task = ""
        while new_task != "no":
            new_task = str(input("Enter your new task enter no to quit: "))
            add_task(new_task)
        print("""
      1. Add a task
      2. Display task lists
      3. Check the next task
      4. Mark task as complete
      5. Exit""")
        option = int(input("Enter the number of the operation you want to perform."))

    if option == 2:
        display_task_list()
        print("""
      1. Add a task
      2. Display task lists
      3. Check the next task
      4. Mark task as complete
      5. Exit""")
        option = int(input("Enter the number of the operation you want to perform."))

    if option == 3:
        next_task()
        print("""
      1. Add a task
      2. Display task lists
      3. Check the next task
      4. Mark task as complete
      5. Exit""")
        option = int(input("Enter the number of the operation you want to perform."))
    
    if option == 4:
        mark_task_complete()
        print(completed_task)
        print("""
      1. Add a task
      2. Display task lists
      3. Check the next task
      4. Mark task as complete
      5. Exit""")
        option = int(input("Enter the number of the operation you want to perform."))