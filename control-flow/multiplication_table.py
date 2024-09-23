# Multiplication Table

# Prompting the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Loop to generate the multiplication table from 1 to 10
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")

# Drawing Pattern

# Prompting the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Use a while loop to iterate through each row
row = 0
while row < size:
    # For loop to print stars in each row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after printing a row
    print()
    row += 1

# Personal Daily Reminder

# Prompting the user for the task, priority, and time sensitivity
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using if-else statements based on the priority
if priority == "high":
    reminder = f"'{task}' is a high priority task"
elif priority == "medium":
    reminder = f"'{task}' is a medium priority task"
elif priority == "low":
    reminder = f"'{task}' is a low priority task"
else:
    reminder = f"'{task}' has an unknown priority"

# Modify the reminder based on whether the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("Reminder:", reminder)

