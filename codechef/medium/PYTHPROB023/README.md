# PYTHPROB023

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked example - Divide Apples Among Friends

In this example, we have 25 candies to distribute among 4 children. Using Integer Division (//), we can quickly find out how many whole candies each child receives, ignoring any leftover candies.

Consider the following:

- Total candies: 25
- Number of children: 4

By applying Integer Division, we find out how many candies each child gets.

When executed, the code will display:

```
6

```

This output indicates that each child receives 6 whole candies, with any remainder ignored by Integer Division. This example effectively demonstrates how Integer Division works in Python.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-02T11:57:37.616Z  

```py
# Total number of candies
candies = 25

# Number of children
children = 4

# Use Integer Division (//) to calculate how many whole candies each child gets
candies_per_child = candies // children

# Print the result
print(candies_per_child)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB023)