# PYTHPROB451

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Validate Item Code with Title Case

You have an item code "item-bookOfKnowledge," and you have to check the following

- whether the item code starts with "item-" and
- whether the remaining part after "item-" is in all lowercase letters. To check the remaining letters - you will have to use string slicing

Print true or false for both cases.

### Expected Output

```
True
False

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-27T04:30:20.648Z  

```py
# Declare a string with a single item code
item_code = "item-bookOfKnowledge"


print(item_code.startswith("item-"))

print(item_code.islower())




```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB451)