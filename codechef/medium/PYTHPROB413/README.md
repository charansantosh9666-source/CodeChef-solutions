# PYTHPROB413

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Validate an Employee ID

In this example, we demonstrate how to use Python’s `isalnum()` method to ensure that an employee ID contains only letters and digits. This check is a common requirement in authentication systems to avoid invalid characters in user identifiers.

Consider the following variable:

```
empID = "empID_123"

```

When the given code is executed, the output will be:

```
False

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-20T02:33:17.662Z  

```py
# Step 1: Declare the employee ID
employee_id = "empID_123"

# Step 2: Check if the employee ID contains only alphanumeric characters
is_valid = employee_id.isalnum()

# Step 3: Print the result
print(is_valid)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB413)