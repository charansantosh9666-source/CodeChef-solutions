# PYTHPROB199

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Movie Entry Eligibility

In this task, A cinema requires students to meet one of the following conditions to enter a movie:

- The student must be 13 years or older.
- OR they must have a signed parental consent form.

 **Task** 

- Take user input for the student's age (integer).
- Take user input for whether they have parental consent (yes/no).
- Use the or operator to check the given conditions.

Now, let’s write the code for this scenario!

### Sample 1:
Input
Output

```
15
yes
```

```
Entry Allowed
```

### Sample 2:
Input
Output

```
12
no
```

```
Entry Denied
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T02:22:50.494Z  

```py
# Take user input for age and parental consent
age = int(input( ))  # User inputs age
has_parental_consent = input( )  # User inputs yes or no

# Check if the student meets at least one condition

if age>=13 or has_parental_consent=="yes":
    print("Entry Allowed")
else:
    print("Entry Denied")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB199)