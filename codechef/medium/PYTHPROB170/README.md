# PYTHPROB170

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Apple Basket Verification

In this task, you will create a program that checks if the total number of apples in a basket is correct.
The basket starts with some apples, and additional apples can be added.
Your goal is to verify whether the total matches the expected count.

 **Requirements:** 

- Take input for the current number of apples and the number of apples added.
- Add the two numbers to calculate the total apples.
- Use the != operator to check if the total does not match the expected value.
- Print the result.
### Sample 1:
Input
Output

```
10
4
```

```
The basket has the wrong number of apples.
```

### Sample 2:
Input
Output

```
10
5
```

```
The basket has the correct number of apples.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T03:34:26.732Z  

```py
# Step 1: Define the expected number of apples
expected_apples = 15

a=int(input())
b=int(input())

if expected_apples==(a+b):
    print("The basket has the correct number of apples.")
else:
    print("The basket has the wrong number of apples.")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB170)