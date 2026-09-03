# PYTHPROB028

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked example - Find Last Digit

In this example, we demonstrate how to determine the last digit of a number using the modulus operator (%). When a number is divided by 10, the remainder from that division reveals the last digit.

For instance, consider the number 123. To find the last digit, you can use the modulus operator with 10:

```
last_digit = 123 % 10

```

This calculation results in a last digit of 3, since `123 % 10` gives a remainder of 3.

When printed, the output would look like this:

```
The last digit is: 3

```

This example effectively illustrates how to use the modulus operator to isolate the last digit of any integer.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T02:03:06.938Z  

```py
# Declare a variable for the number
number = 12345

# Use the modulus operation to find the last digit
last_digit = number % 10

# Print the result
print(last_digit)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB028)