# PYTHPROB029

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### The Leap Year Concept

In this task, you are required to determine the remainder when a given year is divided by 4, 100, and 400 using the modulus operation.

 **Data Values** 

- year = 2024

 **Expected Output** 
After performing the calculations for the year 2024, your program should print the results as follows:

```
Remainder when 2024 is divided by 4: 0
Remainder when 2024 is divided by 100: 24
Remainder when 2024 is divided by 400: 24

```

Feel free to change the year and observe how the remainders change!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T02:04:10.609Z  

```py
# Declare a variable for the year
year =2024 # Initalize with the given value in question

# Calculate the remainders using the modulus operator
remainder_4 = year%4    # Add operation to calculate remainder when divided by 4
remainder_100 = year%100  # Add operation to calculate remainder when divided by 100
remainder_400 = year%400  # Add operation to calculate remainder when divided by 400

# Print the results
print(f"Remainder when {year} is divided by 4: {remainder_4}")
print(f"Remainder when {year} is divided by 100: {remainder_100}")
print(f"Remainder when {year} is divided by 400: {remainder_400}")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB029)