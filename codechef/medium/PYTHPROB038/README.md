# PYTHPROB038

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked example - Evaluate a Complex Expression

In this example, we explore how to evaluate a complex mathematical expression to understand operation precedence in Python.

Python follows precedence rules, summarized by PEMDAS/BODMAS:

- Exponentiation (**)
- Multiplication (*) and Division (/)
- Addition (+) and Subtraction (-), evaluated from left to right.

Consider the expression:

```
result = 10 + 2 * 5 - 3 ** 2

```

When evaluated, the expression computes as follows:

- The exponent (3^2) results in 9.
- The multiplication (2 * 5) results in 10.
- Then, the addition and subtraction are performed in sequence.

The final result illustrates how operation precedence affects the outcome of mathematical expressions in Python.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T02:39:29.139Z  

```py
# This code demonstrates the evaluation of a mathematical expression 
# with multiple operators, considering the order of operations (precedence).

result = 10 + 2 * 5 - 3 ** 2  # Calculate the result according to operator precedence 
print(result) 
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB038)