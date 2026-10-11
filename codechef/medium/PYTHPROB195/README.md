# PYTHPROB195

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Trip Eligibility Based on Grades and Attendance

A school is organizing a trip, and students must meet specific criteria to be eligible. The eligibility requirements are:

- Grade Requirement: The student must have a grade of at least 75.
- Attendance Requirement: The student must have an attendance percentage of at least 85%.

Take grade and attendance input from the user.

### Sample 1:
Input
Output

```
80
90
```

```
Eligible for the school trip.

```

### Sample 2:
Input
Output

```
70
90
```

```
Not eligible for the school trip.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T02:20:59.634Z  

```py
# Prompt the user to input their grade and attendance percentage
a=int(input())
b=int(input())

# Check eligibility based on grade and attend
if a>=75 and b>=75:
    print("Eligible for the school trip.")
else:
    print("Not eligible for the school trip.")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB195)