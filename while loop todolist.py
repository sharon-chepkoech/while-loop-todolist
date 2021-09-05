#this will request a user to input the activities to be done.
#then print them out at the end
todolist = []
while True:
    activity =(input("Enter activity to do"))
    todolist.append(activity)
    choice = input(" Type yes or any other key to continue typing activity")
    if choice == "yes":
        break
print(todolist)
