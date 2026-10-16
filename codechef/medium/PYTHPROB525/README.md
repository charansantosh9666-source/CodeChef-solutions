# PYTHPROB525

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Classify Age Groups

Write a program that determines the age group of a person based on their age.

- 0-12 → Print Child
- 13-19 → Print Teenager
- 20-64 → Print Adult
- 65 or higher → Print Senior
- Use an else statement to print `Invalid age input` if the entered age is negative or not valid.

 **Task** 

- Take age as input from the user and store a value in variable age and Convert the input to an integer.
- Use.strip() to remove extra spaces.
- Convert the output to uppercase using.upper() before printing.
### Sample 1:
Input
Output

```
65
```

```
SENIOR
```

### Sample 2:
Input
Output

```
-45
```

```
INVALID AGE INPUT

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-15T02:36:28.514Z  

```py
age = int(input( ).strip())

# Check the age category using if-elif-else statements
if 0 <= age <= 12:
    print("Child".upper())  # Convert output to uppercase
elif 13 <= age <= 19:
    print("Teenager".upper())  # Convert output to uppercase
elif 20 <= age <= 64:
    print("Adult".upper())  # Convert output to uppercase
elif age >= 65:
    print("Senior".upper())  # Convert output to uppercase
else:
    print("Invalid age input".upper())
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB525)