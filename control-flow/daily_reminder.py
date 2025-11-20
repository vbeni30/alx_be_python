# daily_reminder.py

# Prompt the user for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case for priority
match priority:
    case "high":
        priority_text = "high priority"
    case "medium":
        priority_text = "medium priority"
    case "low":
        priority_text = "low priority"
    case _:
        priority_text = "unknown priority"

# Modify based on time sensitivity
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_text} task that requires immediate attention today!")
else:
    print(f"Reminder: '{task}' is a {priority_text} task. It is not time-bound, so you can complete it when you have free time.")
