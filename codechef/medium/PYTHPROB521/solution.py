# Take user input for age, remove extra spaces, and convert it to an integer
age = int(input( ).strip())  

# Use if-elif structure to classify fitness level based on age

# If age is less than 18, classify as "Young Athlete"
if age<18:
    print("Fitness Level: Young Athlete")

# If age is between 18 and 40 (inclusive), classify as "Active Adult"
elif age>=18 and age<=40:
    print("Fitness Level: Active Adult")

# If age is between 41 and 59 (inclusive), classify as "Health Conscious"
elif age>=41 and age<=59:
    print("Fitness Level: Health Conscious")
