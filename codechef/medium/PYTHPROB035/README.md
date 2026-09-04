# PYTHPROB035

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### My Social Media Viral Post

In this task, you are required to create a program that calculates how many people share a social media post on a given day.

Initially, 10 people shared the post.
Each subsequent day, the total shares tripled (30 shares by the end of the first day, 90 by the end of the second, and so on).

Calculate and print how many people share the post on the 4th day using the given formula.

### Expected output

```
On day 4, the post will be shared by 810 people.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T02:39:05.065Z  

```py
# Initial number of shares on the first day
initial_shares = 10

# Day for which to calculate the number of shares
day = 4 
initial_shares *=pow(3,day)
print(f"On day {day}, the post will be shared by {initial_shares} people.")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB035)