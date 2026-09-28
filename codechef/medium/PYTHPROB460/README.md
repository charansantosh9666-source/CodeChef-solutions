# PYTHPROB460

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Format Employee Numbers

You have a customer name, "alice", and an invoice number "987".

The invoice number must always be displayed with six digits by adding leading zeros if needed, and the customer’s name should be shown in uppercase.

Update the code in the IDE based on the comments provided.

### Expected Output

```
INVOICE FOR ALICE: #000987

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-28T01:52:49.135Z  

```py
customer_name = "alice"   # Given customer name
invoice_number = "987"     # Given invoice number

invoice_number=invoice_number.zfill(6)

print(f"INVOICE FOR ALICE: #{invoice_number}")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB460)