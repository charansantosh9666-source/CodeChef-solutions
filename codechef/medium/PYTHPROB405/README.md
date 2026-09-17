# PYTHPROB405

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Validate Name

In a simple booking system, users might enter their names with digits or special characters by mistake. You need to verify that the first and last names contain only alphabets using the isalpha() method, then properly format the full name by converting it to title case.

You have the following values:
`first_name` : `"john"`
`last_name` : `"doe3"`

 **Expected Output** 
If first name is "Jack" and last name is "daniel", your program might display:

```
True
False
John Doe3

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-17T01:13:40.758Z  

```py
# Declare first name and last name
first_name = "john"
last_name = "doe3"
com=first_name+" "+last_name
# Check if names contain only alphabets

first_valid=first_name.isalpha()
last_valid=last_name.isalpha()
formatted_name=com.title()
# Convert names to title case




# Print results
print(first_valid)
print(last_valid)
print(formatted_name)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB405)