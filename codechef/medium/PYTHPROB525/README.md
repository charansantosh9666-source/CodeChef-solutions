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
**Submitted:** 2026-10-15T02:34:41.879Z  

```py
# Take user input for age, remove extra spaces, and convert it to an integer
a=int(input())

# Check the age category using if-elif-else statements
b="Child"
c="Teenager"
d="Adult"
e="Senior"
# Dont forget to output in uppercase
if a>=0 and a<=12:
    print(b.upper())
elif a>=13 and a<=19:
    print(c.uppper())
elif a>=20 and a<=64:
    print(d.upper())
elif a>=65:
    print(e.upper())
else:
    print("INVALID AGE INPUT")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB525)