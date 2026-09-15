# PYTHPROB400

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Trim Spaces from a Product Title

In this task, you are required to remove unwanted trailing symbols from a product name in an online store and then measure the length of the cleaned name.

You have the following details:

`product_name` = `"Shampoo$$$"`.

 **Expected Output** 
After performing the calculations, your program should print the results as follows:

```
Shampoo
7

```

Feel free to change the value of `product_name` to see how the output updates!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T09:06:21.696Z  

```py
# Step 1: Declare the product name with trailing '$' symbols
product_name = "Shampoo$$$"

c=product_name.rstrip('$')
print(c)
print(len(c))

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB400)