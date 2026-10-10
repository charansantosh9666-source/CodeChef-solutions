# PYTHPROB160

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Determine Even or Odd

In this task, you will create a program for a birthday party organizer to determine whether a participant's age is even or odd.

 **Requirements:** 

- Prompt the user to input the participant's age as an integer.
- Use the modulo operator (%) to check if the age is even or odd:
- Use an if-else statement to implement this logic.
- Make sure to use the.strip() function to remove any extra spaces from the input before processing it.
### Sample 1:
Input
Output

```
23
```

```
Your age is odd!
```

### Sample 2:
Input
Output

```
20
```

```
Your age is even!
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T03:29:33.318Z  

```py
# Step 1: Take input for the participant's age
age = int(input().strip())  # Input the participant's age

if age%2==0:
    print("Your age is even!")
    
else:
    print("Your age is odd!")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB160)