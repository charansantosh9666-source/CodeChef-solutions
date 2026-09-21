# PYTHPROB415

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Validate and Clean an Address

In this task, you are required to check if an address string is alphanumeric and strip away any leading or trailing spaces for clean formatting.

 **Data Values** 
`address = " 1234 Elm St. "`

 **Expected Output** 
For the address `" 1234 Elm St. "`, your program should display:

```
False
1234 Elm St.

```

Feel free to change the address and observe how the results change!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T01:41:43.688Z  

```py
# Declare the address string
address = "    1234 Elm St. "

# Check if the address contains only alphanumeric characters 

is_alphanumeric=address.isalnum()
# Clean the address by stripping leading and trailing spaces
cleaned_address=address.strip() 

# Print the results
print(is_alphanumeric) 
print(cleaned_address)

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB415)