# PYTHPROB388

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Clean Up Username

In this example, we demonstrate how to use Python’s `strip()` method to remove accidental spaces before or after a username. The `strip()` method ensures usernames are stored correctly without leading or trailing whitespace.

Consider the following variable:

```
username = "   TigerKing "

```

When the given code is executed, the output will be:

```
   TigerKing 
TigerKing

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T08:50:16.260Z  

```py
# Step 1: Declare the username with extra spaces
username = "  TigerKing  "

# Step 2: Print the original username (with spaces)
print(username)

# Step 3: Remove leading and trailing spaces using strip()
cleaned_username = username.strip()

# Step 4: Print the cleaned username
print(cleaned_username)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB388)