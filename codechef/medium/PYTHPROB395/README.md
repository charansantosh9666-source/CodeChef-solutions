# PYTHPROB395

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Clean Up a Messy Address

You have a customer address that starts with one or more hash marks (#), "####123 Baker Street".

You need to remove these leading symbols using lstrip(), then measure the length of the cleaned address using len().

Review the comments given in the IDE and output to the console as required.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T08:58:54.289Z  

```py
# Step 1: Declare the messy address with leading symbols
messy_address = "####123 Baker Street"

c=messy_address.lstrip('#')
print(c)
print(len(c))
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB395)