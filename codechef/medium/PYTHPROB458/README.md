# PYTHPROB458

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Format Invoice Numbers

In this example, we demonstrate how to use Python’s `zfill()` method to format an invoice number into a fixed width. This is a common requirement in systems where invoice numbers must be zero-padded to a certain length.

Consider the following variable:

```
invoice_number = "7"

```

When the given code is executed, the output will be the padded invoice number:

```
007

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-27T04:35:24.481Z  

```py
# Assigning the invoice number as a string
invoice_number = '7'

# Using zfill() to pad the invoice number to a width of 3, filling with leading zeros
formatted_invoice = invoice_number.zfill(3)

# Printing the formatted invoice number
print(formatted_invoice)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB458)