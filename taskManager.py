#prints out options
def printOptions():
    print("-----Task Manager-----")
    print("1. Add a Task")
    print("2. Add a Step to a Task")
    print("3. Mark Step as Completed")
    print("4. View all Tasks")
    print("5. Remove a Task")
    print("6. Display Total Number of Tasks")
    print("7. Quit ")

def addTask():
    tasks = {}
    task = input("Enter the task name: ")
    tasks[task] = task
    print("Task '",task,"' added successfully")
    print("")
    print(tasks)

def addStep():
    taskName = input("Enter the task name to add a step to: ")
    taskDescription = input("Enter the step description: ")
    print("Step", taskDescription,"added to task", taskName)
    print("")

def markStep():
    nameCompleted = input("Enter the task name to mark a step as completed: ")
    descriptionCompleted = input("Enter the step description to mark as completed: ")
    print("Step",descriptionCompleted, "in task", nameCompleted, "marked as completed.")
    print("")

def viewTasks():
    print("---- All Tasks ----")

# def removeTask():
#     del tasks[}

def numOfTasks():
    print("Placeholder")

#main function
def main():
    while True:
        printOptions()
        choice = input("Choose an option (1-7): ")
        if choice == "1":
            addTask()
        elif choice == "2":
            addStep()
        elif choice == "3":
            markStep()
        # elif choice == "4":
        #     viewTasks()
        # elif choice == "5":
        #     removeTask()
        # elif choice == "6":
        #     numOfTasks()
        elif choice == "7":
            print("Goodbye!")
            break
        else: 
            print("Incorrect, please enter a valid choice.")

main()