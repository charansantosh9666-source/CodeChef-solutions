# PYTHPROB228

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked Example - Play with Scientific Numbers

In this example, we demonstrate how to convert both very large and very small numbers into scientific notation for better readability.

Consider the following numbers:

- A very large number: 9876543210000000.0
- A very small number: 0.000000012345

To convert these numbers to scientific notation, you can apply the following format specifier `:.3e` in an f-string or use the `format()` function.

When executed, the output for these numbers in scientific notation will appear as:

```
Large number in scientific notation: 9.877e+15
Small number in scientific notation: 1.235e-08

```

This example illustrates how to effectively represent numbers in scientific notation in Python.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T01:36:16.466Z  

```py
# Define the numbers
large_number = 9876543210000000.0
small_number = 0.000000012345

# Convert the numbers to scientific notation with 3 decimal places
large_number_scientific = f"{large_number:.3e}"
small_number_scientific = f"{small_number:.3e}"

# Print the results with meaningful labels
print(f"Large number in scientific notation: {large_number_scientific}")
print(f"Small number in scientific notation: {small_number_scientific}")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB228)