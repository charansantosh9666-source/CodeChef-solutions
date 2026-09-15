# PYTHPROB383

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Check Cases of Animal Names

In this example, we demonstrate how to use the string methods `.isupper()` and `.islower()` to verify whether certain animal names are written entirely in uppercase or lowercase. These checks can be useful for ensuring consistent formatting within your program.

Consider the following animal names:

```
animal1 = "LION"
animal2 = "elephant"

```

When the given code is executed, the output will be:

```
LION is in uppercase: True
LION is in lowercase: False
elephant is in uppercase: False
elephant is in lowercase: True

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T08:42:18.136Z  

```py
# Defining animal names
animal1 = "LION"      # Uppercase
animal2 = "elephant"  # Lowercase

# Checking if the strings are uppercase
is_animal1_upper = animal1.isupper()
is_animal2_upper = animal2.isupper()

# Checking if the strings are lowercase
is_animal1_lower = animal1.islower()
is_animal2_lower = animal2.islower()

# Printing the results
print(f'{animal1} is in uppercase: {is_animal1_upper}')
print(f'{animal1} in lowercase: {is_animal1_lower}')
print(f'{animal2} in uppercase: {is_animal2_upper}')
print(f'{animal2} in lowercase: {is_animal2_lower}')
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB383)