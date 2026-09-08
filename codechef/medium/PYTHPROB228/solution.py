# Define the numbers
large_number = 9876543210000000.0
small_number = 0.000000012345

# Convert the numbers to scientific notation with 3 decimal places
large_number_scientific = f"{large_number:.3e}"
small_number_scientific = f"{small_number:.3e}"

# Print the results with meaningful labels
print(f"Large number in scientific notation: {large_number_scientific}")
print(f"Small number in scientific notation: {small_number_scientific}")