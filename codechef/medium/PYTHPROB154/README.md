# PYTHPROB154

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Marathon Qualification Check

A school is organizing a marathon, and it is important for participants to meet a specific distance requirement to qualify for the next round of the competition. To ensure they are prepared, participants must run a minimum distance of  **15 km**.

In this scenario, a participant's covered distance is predefined as  **20 km**. Your task is to write a program that checks whether the participant qualifies based on the distance they have run.

### Sample 1:
Input
Output

```
15
20

```

```
Qualified for next round!
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T03:24:16.196Z  

```py
# Step 1: Define the required distance and participant's distance
required_distance =int(input())# User input - Minimum distance required to qualify 
participant_distance =int(input()) # User input - Distance run by the participant 

# Step 2: Check if the participant qualifies for the next round
if participant_distance >= required_distance:  # Is the participant's distance enough to qualify?
    print("Qualified for next round!")  # Print result if the condition is true

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB154)