# PYTHPROB410

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Validate an Employee ID for Payroll System

In this task, you are required to clean and validate an employee ID by removing unwanted spaces, converting it to uppercase, and checking if it contains only numeric characters.

 **Data Values** 

- employee_id = " e123"

 **Expected Output** 

```
E123
False

```

Feel free to change the employee ID and observe how the output changes!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-20T02:32:25.134Z  

```py
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

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB410)