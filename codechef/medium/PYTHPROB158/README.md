# PYTHPROB158

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Checks which Team wins a cricket

In this example, we will create a program that determines the winner of a cricket match by comparing Team B’s final score to the target score set by Team A.

### Sample 1:
Input
Output

```
200
210

```

```
Team B wins!
```

### Sample 2:
Input
Output

```
210
200
```

```
Team A wins!
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T03:26:10.885Z  

```py
# Step 1: Take user input for Team A's target and Team B's score
team_a_target = int(input())  # Input Team A's target score
team_b_score = int(input())          # Input Team B's score

# Step 2: Use if-else to determine the winner
if team_b_score > team_a_target:  # Check if Team B's score is greater than Team A's target
    print("Team B wins!")         # Output if Team B wins
else:
    print("Team A wins!")         # Output if Team A wins

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB158)