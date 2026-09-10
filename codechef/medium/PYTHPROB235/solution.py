# Step 1: Original temperature readings
temperature_1 = 23.87654321
temperature_2 = 23.8760
temperature_3 = 23.8769

# Step 2: Round the values to 3 decimal places
reading_1=round(temperature_1,3)
reading_2=round(temperature_2,3)
reading_3=round(temperature_3,3)



# Step 3: Calculate the average of the rounded temperatures
average_rounded=(reading_1+reading_2+reading_3)/3

# Step 4: Calculate the difference in average temperatures
original_avg = (temperature_1 + temperature_2 + temperature_3) / 3
average_difference = original_avg - average_rounded



# Step 5: Print the results
print(f"Rounded Temperature 1: {reading_1}°C")
print(f"Rounded Temperature 2: {reading_2}°C")
print(f"Rounded Temperature 3: {reading_3}°C")
print(f"Average Temperature: {average_rounded}°C")
print(f"Difference in Average Temperature: {average_difference:.3f}°C")