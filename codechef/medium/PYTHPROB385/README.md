# PYTHPROB385

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Check if an animal name is uppercase

You have an animal name "elephant". You need to see if it’s already in uppercase. If it’s not, you’ll convert it to uppercase and check again. This demonstrates the isupper() and upper() methods in Python.

### Expected output

```
elephant
False
ELEPHANT
True

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T08:49:00.348Z  

```py
# Step 1: Declare the animal name
animal_name = "elephant"

# Step 2: Check if the animal name is in uppercase
is_upper=animal_name.isupper()

# Step 3: Print the original state and the uppercase check
print(animal_name)
print(is_upper)

# Step 4: Convert the animal name to uppercase
animal_name=animal_name.upper()

# Step 5: Check if the animal name is in uppercase after conversion
is_upper_after=animal_name.isupper()

# Step 6: Print the final state and the uppercase check after conversion
print(animal_name)
print(is_upper_after)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB385)