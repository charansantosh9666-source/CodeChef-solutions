# PYTHPROB404

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Validate Registration Form

A user enters their name in an online registration form. The system uses the `isalpha()` method to validate the input.

Which of the following inputs will return True when checked with `isalpha()`?

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T09:08:15.188Z  

```cpp
# Step 1: Declare a name with unintended characters
user_name = "John123"

# Step 2: Check if the name contains only alphabets
is_valid = user_name.isalpha()

# Step 3: Print the validity check result
print(is_valid)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB404)