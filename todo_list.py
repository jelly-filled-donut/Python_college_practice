import os
import sys
import datetime as dt


tasks = []
os.system("cls")
today = dt.date.today()

while True:
    print (" Todo list")
    print ("   Menu")
    print ("1. Add a task")
    print ("2. Delete a task")
    print ("3. View tasks")
    print ("4. Sort tasks")
    print ("5. Exit")
    index = 0
    option = 0
    try:
        option = int (input(" Choose an option: "))
    except ValueError:
        print ("Wrong input")
    if option == 1:
        task = input (" Enter a task: ")
        while True:
            try:
                day = int(input(" Enter day for the task: "))
                if day < 1 or day > 31:
                        print("Invalid day, try again!")
                        continue
                month = int(input(" Enter month for the task: "))
                if month < 1 or month > 12:
                        print("Invalid month, try again!")
                        continue
                year = int(input(" Enter year for the task: "))
                if year < today.year:
                        print("Invalid year, try again!")
                        continue
                tasksdate = dt.date(year, month, day)
                break
            except ValueError:
                print()
                print("Invalid date, try again!")
        tasks.append([task, tasksdate])
    if option == 2:
        print(" Current tasks:")
        for i in range(0, len(tasks)):
            print(i + 1, tasks[i][0], tasks[i][1])
        id = int (input(" Choose task to delete: "))
        if id >0 and id <= len(tasks):
            print(" Do you want to delete task: ", tasks[id-1][0], tasks[id-1][1], "?")
            while True:
                print("   Yes / No?   ")
                opt = input("")
                if opt.lower() == "y" or opt.lower() == "yes":
                    print("task :", tasks[id-1][0], tasks[id-1][1], " successfully deleted")
                    del tasks[id-1]
                    break
                elif opt.lower() == "n" or opt.lower() == "no":
                    print("Deleting cancelled")
                    break
                else:
                    print("Invalid input.")
        else:
            print("Invalid task number.")
    if option == 3:
        print(" Current tasks:")
        for i in range(0, len(tasks)):
            print(i + 1, tasks[i][0], tasks[i][1])
    if option == 4:
      tasks.sort(key=lambda x: (x[1] > today, abs((x[1] - today).days)))
      print("Tasks sorted.")
    if option == 5:
        print(" Do you want to exit the program?")
        while True:
            print("   Yes / No?   ")
            opt = input("")
            if opt.lower() == "y" or opt.lower() == "yes":
                print("Exiting the program.")
                os.system("cls")
                sys.exit()
            elif opt.lower() == "n" or opt.lower() == "no":
                print("Exit cancelled.")
                break
            else:
                print("Invalid input. Exit canceled.")
                break
    input("Press Enter to continue...")
    os.system("cls")


#done