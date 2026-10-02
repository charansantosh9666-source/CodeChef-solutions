# User enter their favorite color and number
user_input = input()

# Spliting the input into color and number
favorite_color, favorite_number = user_input.split()

# now convert the number to an integer
favorite_number = int(favorite_number)

# print the friendly message
print(f"Your favorite color is {favorite_color} and your favorite number is {favorite_number}.")