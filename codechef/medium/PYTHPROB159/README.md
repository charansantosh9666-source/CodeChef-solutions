# PYTHPROB159

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Check if a number is positive or negative

In this problem, you will create a program that determines whether a given number is positive or negative. The predefined number for this exercise is  **5**.

 **Requirements:** 

- Define a variable called number to store the given number.
- Use an if-else statement to check the value of the number: If the number is greater than or equal to zero, the program should output: "The number is positive." If the number is less than zero, the program should output: "The number is negative."
### Sample 1:
Input
Output

```
5
```

```
The number is positive.
```

### Sample 2:
Input
Output

```
-3
```

```
The number is negative.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T03:27:49.008Z  

```py
# Step 1: Define the number
number = int(input())    # User input

if number>=0:
    print("The number is positive.")
    
else:
    print("The number is negative.")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB159)