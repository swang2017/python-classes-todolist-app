
tasks = []

class Task:
    def __init__(self, taskNumber, description, priority):
        self.taskNumber = taskNumber
        self.description = description
        self.priority = priority

    def __repr__(self):
        return (str(self.taskNumber) + " : " + self.description + " : " + self.priority)


def addTask(task):
    tasks.append(task)
def removeTask(task):
    tasks.remove(task)
def viewTasks():
    print("the tasks are \n {0}".format(tasks))


count = 0

while True:


    input_options = raw_input("please input what you want to do: \n1 to add task, 2 to remove task, 3 to view tasks, q to quit the program\n")
    if input_options == "1":
        add_task = raw_input("please enter the task you want to add\n")
        add_priority=raw_input("please enter the priority\n")
        count += 1
        task1 = Task(count, add_task,add_priority)
        addTask(task1)
        viewTasks()
    elif input_options == "2":
        remove_task = int(raw_input("please enter the task number you want to remove\n"))
        for index in range (0,len(tasks)):
            if remove_task == tasks[index].taskNumber:
                removeTask(tasks[index])

                break
        viewTasks()
    elif input_options == "3":
        viewTasks()
    elif input_options == "q":
        break
