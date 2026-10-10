# PYTHPROB168

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Cricket Match Decision

In this example, we will create a program that checks if Team B's score matches the target set by Team A using the `!=` operator.

### Sample 1:
Input
Output

```
250
240
```

```
Team B did not match the target.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T03:32:02.893Z  

```py
# Step 1: Define Team A's target and Team B's score
team_a_target = int(input())  # Team A's target score
team_b_score = int(input())   # Team B's score

# Step 2: Check if the scores are different using the != operator
if team_b_score != team_a_target:
    print("Team B did not match the target.")  # Output if scores are different
else:
    print("Team B matched the target.")  # Output if scores are the same


```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB168)