# PYTHPROB384

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Validate the Case of Animal Name

A zookeeper is entering animal names into a database. To ensure consistency, all predator names must be in uppercase, while all herbivore names must be in lowercase.

Given the following code snippet:

```
predator = "TIGER"
herbivore = "giraffe"

print(predator.isupper())  
print(herbivore.islower())

```

 **What will be the output of the above code?**

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T08:44:26.508Z  

```cpp
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

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB384)