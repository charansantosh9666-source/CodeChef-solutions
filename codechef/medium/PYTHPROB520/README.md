# PYTHPROB520

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Fitness Level Classification Based on Age

A fitness trainer wants to classify individuals into different fitness levels based on their age. The program will prompt the user to enter their age, process the input correctly, and determine their fitness category using the if-elif structure.

 **Task** 

- Take the user's age as input using input() and remove extra spaces using.strip().
- Convert the input to an integer using int().

 **Use the if-elif structure to classify the user into a fitness category** :

- Young Athlete (Below 18 years) → Print Fitness Level: Young Athlete
- Active Adult (18 to 40 years) → Print Fitness Level: Active Adult
- Health Conscious (41 to 59 years) → Print Fitness Level: Health Conscious
- Ensure the program correctly processes user input using.strip(), making it more reliable.

Now it's your turn! Write the code and check which fitness level you belong to!

### Sample 1:
Input
Output

```
45
```

```
Fitness Level: Health Conscious
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-12T02:53:38.965Z  

```py
# Take user input for age, remove extra spaces, and convert it to an integer
age = int(input( ).strip())  

# Use if-elif structure to classify fitness level based on age

# If age is less than 18, classify as "Young Athlete"
if age<18:
    print("Fitness Level: Young Athlete")

# If age is between 18 and 40 (inclusive), classify as "Active Adult"
elif age>=18 and age<=40:
    print("Fitness Level: Active Adult")

# If age is between 41 and 59 (inclusive), classify as "Health Conscious"
elif age>=41 and age<=59:
    print("Fitness Level: Health Conscious")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB520)