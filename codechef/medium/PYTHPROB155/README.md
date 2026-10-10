# PYTHPROB155

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### You passed the exam!

A school is conducting an exam, and it is essential for students to achieve a minimum score to pass.
The goal is to determine if a student has successfully passed the exam based on their score.

 **Requirements:** 

- Define the minimum passing mark as 40.
- Take the student's score as input from the user.
- Use an if statement to check if the student's score is greater than or equal to the passing mark.
- If the score meets or exceeds the passing mark, print: "You passed the exam!". If the score is below the passing mark, the program should do nothing.
### Sample 1:
Input
Output

```
45
```

```
You passed the exam!
```

### Sample 2:
Input
Output

```
35
```

```
 
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T03:25:44.759Z  

```py
# Define the minimum passing mark
minimum=40

# Take the student's score as input
student=int(input())

# Check if the score is greater than or equal to the passing mark
if student>=minimum:
    print("You passed the exam!")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB155)