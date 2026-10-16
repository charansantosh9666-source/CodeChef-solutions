age = int(input( ).strip())

# Check the age category using if-elif-else statements
if 0 <= age <= 12:
    print("Child".upper())  # Convert output to uppercase
elif 13 <= age <= 19:
    print("Teenager".upper())  # Convert output to uppercase
elif 20 <= age <= 64:
    print("Adult".upper())  # Convert output to uppercase
elif age >= 65:
    print("Senior".upper())  # Convert output to uppercase
else:
    print("Invalid age input".upper())