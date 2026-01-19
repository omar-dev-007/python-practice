"""
Age Calculator
---------------
This program takes the user's birth year as input
and calculates their current age.
"""

# Ask the user for their birth year
birth_year = input("Enter your birth year: ")

# Convert input to integer and calculate age
current_year = 2026
age = current_year - int(birth_year)

# Display the result
print("Your age is:", age)


