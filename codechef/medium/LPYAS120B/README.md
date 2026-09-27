# LPYAS120B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program to calculate the sum of first  **N**  multiples of 3 and print it.

Check the sample input / output below for further clarity.

### Input Format
- The only input is an integer N.
### Output Format
- The only output is the sum of first N multiples of 3.
### Sample 1:
Input
Output

```
4
```

```
30
```

### Explanation:

First 4 multiples of 3 are: 3, 6, 9 and 12
Hence, 3 + 6 + 9 + 12 = 30

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-27T05:18:40.306Z  

```py
N = int(input())
ans=0
# Update the code below this line
for i in range(1,N+1):
    ans+=3*i
    
print(ans)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS120B)