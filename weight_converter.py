"""
Weight Converter
----------------
This program converts weight from pounds (lbs)
to kilograms (kg).
"""

# Conversion factor from pounds to kilograms
POUND_TO_KG = 0.45359237

# Ask the user for weight in pounds
weight_pounds = input("Enter weight in pounds: ")

# Convert input to integer and calculate weight in kg
weight_kg = int(weight_pounds) * POUND_TO_KG

# Display the result
print("Weight in kilograms is:", weight_kg)
