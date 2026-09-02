# LPYAS139

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a function named  **calculatePower**  that takes two integer,  **base**  and  **exponent**  respectively, and returns the result of raising  **base**  to the power of  **exponent** 

### Sample 1:
Input
Output

```
2 3
```

```
8
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-02T12:54:43.473Z  

```py
def calculate_power(base, exponent):
    ans=1
    #write your code here
    while exponent>0:
        ans=ans*base
        exponent=exponent-1
    return ans
    
    
def main():
    base, exponent = map(int, input().split())
    result = calculate_power(base, exponent)
    print(result)


main()

```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS139)