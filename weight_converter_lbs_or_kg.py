"""
Weight Converter
----------------
This program converts weight:
- from pounds (lbs) to kilograms (kg)
- from kilograms (kg) to pounds (lbs)
"""

# Ask the user to enter their weight
weight = int(input("Enter your weight: "))

# Ask the user to choose the unit of the entered weight
# L = pounds (lbs)
# K = kilograms (kg)
unit = input("Please select unit lbs (L) or kg (K): ")

# Convert the unit input to uppercase so both 'l' and 'L' work
if unit.upper() == "L":
    # If weight is in pounds, convert it to kilograms
    converted = weight * 0.45
    print(f"Your weight in kilograms is { converted}")
else:
    converted = weight / 0.45
    print(f"Your weight in pounds is {converted}")
