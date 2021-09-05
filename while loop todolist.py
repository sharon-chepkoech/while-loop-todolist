todolist = []
while True:
    activity =(input("Enter activity to do"))
    todolist.append(activity)
    choice = input(" Type yes or any other key to continue typing activity")
    if choice == "yes":
        break
print(todolist)