# PYTHPROB193

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Meeting Attendance Check

In this example, we will create a program to determine if an employee qualifies for a bonus based on their work performance metrics.

- Condition 1: completed_hours >= 40 evaluates to True since 42 is greater than or equal to 40.
- Condition 2: attended_meetings >= 5 evaluates to True since 6 is greater than or equal to 5.
- and Operator: Both conditions are True, so the final result is True and the message "Employee qualifies for the bonus." is printed.
- If both conditions are met, the program prints True, otherwise False.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T03:34:57.150Z  

```py
# Define the completed hours and meetings attended
completed_hours = 42  
attended_meetings = 6

# Check bonus eligibility using if-else statement
if completed_hours >= 40 and attended_meetings >= 5:
    print(True)  # If both conditions are met, print True
else:
    print(False)  # If any condition is not met, print False

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB193)