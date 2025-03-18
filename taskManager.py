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
    task = input("Enter the task name: ")
    print("Task,'",task,"' added successfully")



def choices():
    choice = input("Choose an option (1-7): ")
    if choice == "1":
        addTask()


#main function
def main():
    printOptions()
    choices()

main()