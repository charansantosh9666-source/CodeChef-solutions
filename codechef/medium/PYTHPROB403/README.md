# PYTHPROB403

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Check if a name is valid

In this example, we demonstrate how to use Python’s `isalpha()` method to verify if a user’s name contains only alphabetical characters. This check is common in registration forms where usernames should not include digits or special characters.

Consider the following variable:

```
user_name = "John123"

```

When the given code is executed, the output will be:

```
False

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T09:07:05.863Z  

```py
# Step 1: Declare a name with unintended characters
user_name = "John123"

# Step 2: Check if the name contains only alphabets
is_valid = user_name.isalpha()

# Step 3: Print the validity check result
print(is_valid)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB403)