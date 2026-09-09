# Step 1: Original length in millimeters
original_length = 7.123456789

# Step 2: Round the value to 4 decimal places
rounded_length = round(original_length,4)

# Step 3: Calculate the difference in precision
precision_difference = original_length - rounded_length
# Step 4: Update the blanks in the code below
print(f"Rounded length: {rounded_length}")
print(f"Difference in precision: {precision_difference:.4f}")
