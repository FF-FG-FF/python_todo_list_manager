def display_menu():
    print("1. ADD TASK")
    print("2. VIEW TASK")
    print("3. COMPLETE TASK")
    print("4. DELETE TASK")
    print("5. EXIT")
    
def add_task(tasks):
    task = input("Enter A Task: ")
    tasks.append(task)
    print("Task Added Succesfully")
    
def view_task(tasks):
    if len(tasks)==0:
        print("no tasks found")
    else:
        print("Tasks: ")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}, {task}")
            
def mark_complete(tasks):
    view_task(tasks)
    task_index = int(input("Enter The Index Task Number for the task you wish to complete"))
    
    if task_index < 1 or task_index > len(tasks):
        print("Invalid Index Task Number")
    else:
        completed_task = tasks.pop(task_index - 1)
        print(f"you have marked complete ' {completed_task} ' ")
        
def delete_task(tasks):
    view_task(tasks)
    task_index = int(input("Enter The Index Number for the task you wish to delete"))
    
    if task_index < 1 or task_index > len(tasks):
        print("Invalid Index Task Number")
    else:
        delete_task = tasks.pop(task_index - 1)
        print(f"you have deleted {delete_task}") 
        
def todo_list_manager():
    tasks = []
    
    while True:
        display_menu()
        choice = int(input("Enter A SHORTCUT Number: "))
        
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_task(tasks)
        elif choice == 3:
            mark_complete(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            print("Exiting The program GOODBYE!")
            break
        else:
            print("Invalid Choice Please try again")

todo_list_manager()            
