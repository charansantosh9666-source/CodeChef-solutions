# PYTHPROB420

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Locate bird in a bird-watching note

You have a product description like "Latest Model - X45Pro is now available in stock!" and a known product code such as "X45Pro".

You need to locate the substring "X45Pro" in the product description and also convert the product code to uppercase.

Output the index and the uppercase value of the substring to the console.

### Expected output

```
15
X45PRO

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T16:34:27.656Z  

```py
# Declare the product description
product_description = "Latest Model - X45Pro is now available in stock!"

# Declare the product code
product_code = "X45Pro"

# Find the index of the product code in the description
index=product_description.find(product_code)

# Convert the product code to uppercase
product_code.upper()

# Print the results
print(index)
print(product_code)

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB420)