#define variable and prompt user to input task
Task = input("Enter task description:")
Time_Bound = input("Is it time-bound? (yes/no):")
Priority = input("priority (high,medium,low:)")


#match case stetament with priority
match Priority:
    case "high":
        print(f"Reminder: '{Task}'is a high priority task", end="")
        if Time_Bound == "yes":
         print("that requires immediate attention today!")
        else:
         print("but can be done anytime today.")

    case "medium":
        print(f"Reminder: '{Task}'is a medium priority", end="")
        if Time_Bound == "yes":
         print(" that requires attention soon!")
        else:
         print(" but make sure you finish it by the end of the day.")
    case "low":
        print(f"Reminder: '{Task}' is a low priority", end="")
        if Time_Bound == "yes":
         print("but it is time-sensitive, so try to complete it soon!")
        else:
         print(" and can be completed whenever you have free time.")
    case _:
        print("Invalid priority level! Please choose from high, medium, or low.")


     
     
        