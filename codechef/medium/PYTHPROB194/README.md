# PYTHPROB194

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Age and Membership Access Check

A fitness center is organizing a special challenge and wants to determine if participants are eligible based on the following criteria:

- Age Requirement: Participants must be between 18 and 50 years old, inclusive.
- Membership Status: Participants must have an active membership.

You will need to take the input for the age from the user, as well as the membership status.

### Sample 1:
Input
Output

```
20
True
```

```
Access granted
```

### Sample 2:
Input
Output

```
17
False
```

```
Access denied
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T02:18:43.628Z  

```py
# Define the age of the user
age = int(input()) 

# Define if the user is an active member
is_active_member = input() 

# Check if the user is eligible based on age and membership status

if age>=18 and age<=50 or is_active_member ==True:
    print("Access granted")
else:
    print("Access denied")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB194)