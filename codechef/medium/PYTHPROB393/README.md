# PYTHPROB393

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Clean up a messy mission name

In this example, we demonstrate how to use Python’s `lstrip()` method to remove leading asterisks from mission names. This ensures that the mission names are formatted correctly without any unnecessary characters at the start.

Consider the following variable:

```
mission_name = "***APOLLO 11"

```

When the given code is executed, the output will be:

```
APOLLO 11

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T08:56:34.718Z  

```py
# Step 1: Declare the mission name with leading asterisks
mission_name = "***APOLLO 11"

# Step 2: Remove leading asterisks using lstrip()
cleaned_name = mission_name.lstrip('*')

# Step 3: Print the cleaned name
print(cleaned_name)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB393)