# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date
    print(f"Current date and time: {formatted_date}")
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date(current_date):
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    future_date = current_date + timedelta(days=days_to_add)  # Add the number of days
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
    print(f"Future date: {formatted_future_date}")

def main():
    # Display the current date and time
    current_date = display_current_datetime()

    # Calculate and display the future date
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()

