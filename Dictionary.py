print "Welcome to the TODO task management program!"

todo_dict = {}
print todo_dict

while True:
    task = raw_input("Please enter a TODO task: ")
    status = raw_input("Was the task completed? yes/no ")    # yes is boolean True, no is boolean False

    print "Task: " + task + ", Status: " + status

    if status.lower() == "yes":
        todo_dict[task] = True           # adding keys and values to the dictionaries

    else:
        todo_dict[task] = False

    new = raw_input("Would you like to enter another task? yes/no ")

    if new.lower() == "no":
        break


print "Completed tasks: "
for item in todo_dict:
    if todo_dict[item] is True:         # if X == True. With "is" ->simplified
        print "- " + item

print "Uncompleted tasks: "
for item in todo_dict:
    if todo_dict[item] is False:
        print "- " + item
