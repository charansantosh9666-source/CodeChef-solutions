# PYTHPROB233

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Sum with Float Precision

In this example, we calculate the sum of two floating-point numbers—0.1 and 0.2—and observe how Python handles precision.

When you add 0.1 and 0.2 in Python, you may encounter unexpected results due to how floating-point numbers are represented in binary. To present a more intuitive value, rounding the result can be helpful.

For instance, you can perform the addition like this:

```
result = 0.1 + 0.2

```

When you print the raw result, you might notice a minor precision issue. To adjust the output, you can round the result to one decimal place:

```
rounded_result = round(result, 1)

```

The final values will show how rounding can help mitigate floating-point precision issues in Python.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-09T01:12:46.853Z  

```py
# Define the float numbers
num1 = 0.1
num2 = 0.2

# Calculate the sum
result = num1 + num2

# Print the original result
print("Result without rounding:", result)

# Round the result to one decimal place
rounded_result = round(result, 1)

# Print the rounded result
print("Result after rounding:", rounded_result)

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB233)