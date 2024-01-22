#Gabe
#1/18/24
#To-do list Pt.2

todoList = []
print("Which option would you like to choose? \n1.)Option1 = Add Item To List \n2.)Option2 = Show List \n3.)Option3 = Mark As Complete \n4.)Option4 = Remove Item From List \n5.)Option5 = Remove All Itemns on List \n6.)Option6 = Sort List Alphabetlically \n7.)Option7 = Print the Number of Items on The List \n8.)OPtion5 = Exit The Program")
Option = int(input("Which option would you like to choose?"))
while (Option <8):
    Option = int(input("Which option would you like to choose?"))
    if Option == 1:
        Item = input("What should be added to the list?")
        todoList.append(Item)
        print(todoList)
    if Option == 2:
        print(todoList)
    if Option == 3:
        Item = input("Which item would you like to mark as complete?")
        x = todoList.index(Item)
        todoList[x] = (Item + " Completed")
    if Option == 4:
        Item = input("Which item would you like to remove?")
        y = todoList.index(Item)
        todoList.pop(y)
    if Option == 5:
        todoList.clear()
        print(todoList)
    if Option == 6:
        todoList.sort()
        print(todoList)
    if Option == 7:
        print(len(todoList))
    if Option == 8:
        print("You have exited the program.")