from todo_list_pyproj.task import Task

taskList = []

def addTask():
    print("Add task")
    input_name = input("Enter the task name: ")
    input_dueDate = input("Enter the due date: ")
    input_priority = input("Enter the priority: ")
    input_status = input("Enter the status: ")
    task = Task(input_name, input_dueDate, input_priority, input_status)
    taskList.append(task)
    print("Task added successfully!")

def markAsComplete():
    print("Mark as complete")
    input_id = input("Enter the task id: ")
    taskList[int(input_id)-1].setStatus("Complete")
    print("Task marked as complete successfully!")

def removeTask():
    print("Remove task")
    input_id = input("Enter the task id: ")
    taskList.pop(int(input_id)-1)
    print("Task removed successfully!")

def viewTasks():
    print("View tasks")
    for task in taskList:
        print(task.id+1,'-' ,'Name: ',task.name, 'Due date: ', task.due_date, 'Priority: ', task.priority, 'Status: ', task.status)