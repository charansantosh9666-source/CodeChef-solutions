# PYTHPROB163

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Cricket Match Tie Checker

In this example, we will create a program for a cricket scorekeeper to determine if a match ends in a tie. The program compares Team B’s score with the target set by Team A.

### Sample 1:
Input
Output

```
100
100
```

```
The match is tied!
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T03:30:07.097Z  

```py
# Step 1: Define Team A's target and Team B's score
team_a_target = int(input())  # Input target score
team_b_score = int(input())   # Input Team B's score

# Step 2: Compare the scores using the == operator
if team_b_score == team_a_target:
    print("The match is tied!")      # Output if scores are equal
else:
    print("The match is not tied!")  # Output if scores are not equal

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB163)