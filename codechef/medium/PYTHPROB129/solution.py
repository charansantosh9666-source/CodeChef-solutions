# User enters their dream car brand and model (same line)
car_brand, car_model =input().split()        # Splitting string inputs

# User enters the year they want to own the car (new line)
dream_year =int(input())                    # Convert input to integer

# Output the collected information
print(f"You dream of owning a {car_brand} {car_model} in the year {dream_year}.")
