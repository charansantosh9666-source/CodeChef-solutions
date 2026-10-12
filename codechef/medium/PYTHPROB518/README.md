# PYTHPROB518

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Movie Ticket Pricing Based on Age

In this example, we will create a program that classifies a person into different ticket categories based on their age. The cinema charges different ticket prices for children, teens, and adults.

 **The program checks conditions in order:** 

- If the age is 0 to 12, it prints Child Ticket: $5.
- If the age is 13 to 19, it prints Teen Ticket: $8.
- If the age is 20 to 64, it prints Adult Ticket: $12.
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
19
```

```
Teen Ticket: $8
```

### Sample 3:
Input
Output

```
5
```

```
Child Ticket: $5
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-12T02:49:04.413Z  

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

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB518)