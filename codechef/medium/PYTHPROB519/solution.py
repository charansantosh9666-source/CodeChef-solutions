# Take user input for age and convert it to an integer
age = int(input( ))  

# Use if-elif structure to determine the meal category based on age
# If age is 3 or below, recommend a "Toddler Meal"
if age <= 3:  
    print("Recommended Meal Plan: Toddler Meal")

# Else If age is between 4 and 12 (inclusive), recommend a "Kids Meal"
elif age<=12 and age>=4:
    print("Recommended Meal Plan: Kids Meal")

# Else If age is between 13 and 19 (inclusive), recommend a "Teen Meal"
elif age<=19 and age>=13:
    print("Recommended Meal Plan: Teen Meal")

# Else If age is between 20 and 59 (inclusive), recommend an "Adult Meal"
elif age<=59 and age>=20:
    print("Recommended Meal Plan: Adult Meal")