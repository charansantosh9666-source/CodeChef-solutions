# PYTHPROB164

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Locker Code Verification

Imagine, You are creating a program to verify a locker access code. The correct code is stored in the variable correct_code, and the user enters a code, which is stored in the variable entered_code.

Which Python code checks whether the user-entered code matches the correct code and prints 'Access Granted' if they match or 'Access Denied' if they don't?

Option 1:

```
if correct_code == entered_code:
    print("Access Granted")
else:
    print("Access Denied")

```

Option 2:

```
if correct_code = entered_code:
    print("Access Granted")
else:
    print("Access Denied")

```

Option 3:

```
if entered_code === correct_code:
    print("Access Granted")
else:
    print("Access Denied")

```

Option 4:

```
if entered_code != correct_code:
    print("Access Granted")
else:
    print("Access Denied")

```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T03:30:24.082Z  

```cpp
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

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB164)