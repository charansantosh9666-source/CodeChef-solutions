# PYTHPROB435

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Modify Product Description

You have a product description that includes the word "mobile" multiple times, but the platform standards require using the word "smartphone."

Also, descriptions should be in lowercase.

Hence, you’ll both convert the text to lowercase and replace "mobile" with "smartphone."

### Expected Output

```
this smartphone has a powerful processor. smartphone gaming is smooth on this smartphone.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-25T01:53:38.986Z  

```py
# Declare the product description
description = "This mobile has a powerful processor. Mobile gaming is smooth on this mobile."

description=description.lower()

description=description.replace("mobile","smartphone")

print(description)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB435)