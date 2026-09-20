# Step 1: Declare the employee ID
employee_id = " e123"

# Step 2: Remove leading spaces
a=employee_id.lstrip()

# Step 3: Convert the cleaned ID to uppercase
cleaned_employee_id=a.upper()

# Step 4: Check if the cleaned ID contains only digits
is_numeric=cleaned_employee_id.isdigit()

# Step 5: Print the result
print(cleaned_employee_id)
print(is_numeric)
