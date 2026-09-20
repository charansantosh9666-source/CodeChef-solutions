# PYTHPROB409

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Validate the Age

A ticket booking system requires users to enter their age. The system should verify that the input consists only of digits before processing. Given the following user inputs, which one will return False when checked with `isdigit()`?

```
age = "______"
print(age.isdigit())

```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-20T02:28:22.518Z  

```cpp
# User input (simulating a form entry)
age = "25"

# Check if the input contains only digits
is_numeric = age.isdigit()

# Print the result of the check
print(is_numeric)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB409)