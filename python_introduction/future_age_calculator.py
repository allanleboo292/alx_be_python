# Prompt the user for their current age
current_age = int(input("How old are you? "))

# Calculate the user's age in the year 2050
future_year = 2050
current_year = 2023
years_until_future = future_year - current_year
age_in_future = current_age + years_until_future

# Print the result
print(f"In {future_year}, you will be {age_in_future} years old.")
