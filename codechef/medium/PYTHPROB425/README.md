# PYTHPROB425

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Locate a Product Code

You have a product catalog system where each product code is embedded in a longer description.
In this task, you’ll locate the position of a product code ("X500") in the text and find the total length of the description. You need to output the following

- The starting position of the product code.
- The total length of the product description.
### Expected Output

```
26
46

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-22T01:17:11.193Z  

```py
product_description = "New Arrival: Laptop Model X500, available now!"

position=product_description.index("X500")

t=len(product_description)

print(position)
print(t)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB425)