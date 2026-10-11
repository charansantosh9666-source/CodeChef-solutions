# PYTHPROB198

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Employee Bonus Eligibility Check

In this example, we will create a program to determine if an employee qualifies for a bonus based on their completed hours and attendance at mandatory meetings.

The program will check if the employee has either completed at least  **40 hours**  (`completed_hours >= 40`) or attended at least  **5 meetings**  (`attended_meetings >= 5`).
If either condition is met, the employee qualifies for the bonus.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T02:21:21.084Z  

```py
# Predefined variable for the number of hours worked by the employee
completed_hours = 38  # Number of hours worked by the employee

# Predefined variable for the number of meetings attended by the employee
attended_meetings = 6  # Number of meetings the employee has attended

# Check if the employee qualifies for the bonus by verifying if any of the conditions are met:
# 1. If the employee has worked 40 or more hours.
# 2. Or if the employee has attended 5 or more meetings.
if completed_hours >= 40 or attended_meetings >= 5:
    # If either condition is true, print that the employee is eligible for the bonus
    print("Employee is eligible for the bonus.")
else:
    # If neither condition is met, print that the employee is not eligible for the bonus
    print("Employee is not eligible for the bonus.")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB198)