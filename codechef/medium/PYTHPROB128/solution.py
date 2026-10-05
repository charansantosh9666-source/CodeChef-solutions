# Collecting user's dream vacation destination and preferred travel season (same line)
destination, season = input().split()  # Splitting string inputs

# Collecting the number of travel companions and estimated trip duration (same line)
companions, duration = map(int, input().split())  # Splitting and converting numeric inputs

# Output the collected information
print(f"You are planning a trip to {destination} during {season}.")
print(f"You will be travelling with {companions} companions for {duration} days.")
