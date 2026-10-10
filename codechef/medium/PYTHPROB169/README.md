# PYTHPROB169

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Car Speed Check

In this example, You are designing a program to check if a car’s current speed is not equal to the speed limit. The program follows this basic logic:

- If the current speed is not equal to the speed limit, the program prints "The car is not at the speed limit.".
- If the current speed matches the speed limit, the program prints "The car is at the speed limit.".

Option 1:

```
if current_speed != speed_limit:
    print("The car is at the speed limit.")
else:
    print("The car is not at the speed limit.")

```

Option 2:

```
if current_speed != speed_limit:
    print("The car is not at the speed limit.")
else:
    print("The car is at the speed limit.")

```

Option 3:

```
if current_speed =! speed_limit:
    print("The car is not at the speed limit.")
else:
    print("The car is at the speed limit.")

```

Option 4:

```
if current_speed == speed_limit:
    print("The car is not at the speed limit.")
else:
    print("The car is at the speed limit.")

```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T03:32:24.108Z  

```cpp
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

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB169)