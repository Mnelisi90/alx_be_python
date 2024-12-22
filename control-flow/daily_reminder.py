#define variable and prompt user to input task
task = input("Enter task description:")
time_bound = (input("Is the task time bound (yes or no)"))
priority = input("high,medium,low")


#match case stetament with priority
match priority:
    case "high":
        print(f"Reminder: '{task}'is a high priority task", end="")
        if time_bound == "yes":
         print("that requires immediate attention today!")
        else:
         print("but can be done anytime today.")

    case "medium":
        print(f"Reminder: '{task}'is a medium priority", end="")
        if time_bound == "yes":
         print(" that requires attention soon!")
        else:
         print(" but make sure you finish it by the end of the day.")
    case "low":
        print(f"Reminder: '{task}' is a low priority", end="")
        if time_bound == "yes":
         print("but it is time-sensitive, so try to complete it soon!")
        else:
         print(" and can be completed whenever you have free time.")


     
     
        