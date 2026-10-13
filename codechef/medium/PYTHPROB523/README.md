# PYTHPROB523

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Movie Ticket Pricing Based on Age

In this example, we have a cinema that charges different ticket prices based on a person's age. We are going to write a program that classifies a person into different ticket categories using the if-elif structure.

 **The program checks conditions in order:** 

- If the age is 0 to 12, it prints Child Ticket: $5.
- If the age is 13 to 19, it prints Teen Ticket: $8.
- If the age is 20 to 64, it prints Adult Ticket: $12.
- If the age is 65 or above, it prints Senior Ticket: $7.
### Sample 1:
Input
Output

```
50
```

```
Adult Ticket: $12
```

### Sample 2:
Input
Output

```
65
```

```
Senior Ticket: $7
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T12:45:24.859Z  

```py
# Take user input for age and convert it to an integer
age = int(input( ))

# Check the age group using if-elif structure
if age <= 12:
    # If age is 12 or below, print child ticket price
    print("Child Ticket: $5")
elif age <= 19:
    # If age is between 13 and 19, print teen ticket price
    print("Teen Ticket: $8")
elif age <= 64:
    # If age is between 20 and 64, print adult ticket price
    print("Adult Ticket: $12")
else:
    # If age is 65 or above, print senior ticket price
    print("Senior Ticket: $7")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB523)