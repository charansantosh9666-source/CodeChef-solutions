# PYTHPROB394

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Cleaning Up Product Code

A warehouse system has product codes that inadvertently have leading hyphens "----X1234".

You need to remove these hyphens at the start of the string using the lstrip() method — leaving the rest of the code intact.

Output the cleaned product code to the console based on the comments in the IDE.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T08:57:41.073Z  

```py
# Step 1: Declare the product code with leading asterisks
product_code = "----X1234"

print(product_code.lstrip('-'))
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB394)