# PYTHPROB340

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Get all Product IDs

You have a multi-line string representing product codes and product names. For example:

```
products = """12 Smartphone
34 Laptop
56 Tablet"""

```

The goal is to extract and print the first two characters (the product ID) from each line.

### Expected Output

```
12
34
56

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-12T01:12:04.352Z  

```py
# cook your dish here
products = """12 Smartphone
34 Laptop
56 Tablet"""

product_id_1 = products[0] + products[1]  
product_id_2 = products[14] + products[15]  
product_id_3 = products[24] + products[25] 

print(product_id_1)
print(product_id_2)
print(product_id_3)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB340)