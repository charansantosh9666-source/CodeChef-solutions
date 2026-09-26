# PYTHPROB440

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Splitting a Shopping List

You have a shopping list in a string, "milk,bread,eggs,cheese,butter".

You want to split this string into individual items based on commas and also count how many commas appear in the string.

### Expected Output

```
['milk', 'bread', 'eggs', 'cheese', 'butter']
4

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-26T02:04:25.981Z  

```py
# Shopping list string
shopping_list = "milk,bread,eggs,cheese,butter"

shopping=shopping_list.split(",")

print(shopping)

Count=shopping_list.count(",")

print(Count)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB440)