# PYTHPROB225

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Round Final Amount

In this task, you are required to calculate the final amount in USD for a customer exchanging foreign currency.

You have the following details:

- The customer has 3543.876 units of their local currency.
- The current exchange rate is 0.7685 (1 local unit = 0.7685 USD).
- A transaction fee of 12.50 USD is applied after conversion.

Your program should print:

- The amount in USD before fees rounded to 3 decimal places.
- The final amount after fees rounded to 2 decimal places.
### Expected Output

```
Amount before fees (rounded to 3 decimals): 1700.581
Final amount after fees (rounded to 2 decimals): 1689.08

```

Feel free to change the values to see how the calculations affect the final amounts!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T01:35:44.004Z  

```py
# Initial amount in local currency
local_currency = 3543.876  

# Exchange rate (local currency to USD)
exchange_rate = 0.7685  

# Transaction fee in USD
transaction_fee = 12.50  

# Step 1: Convert the local currency to USD
amount_in_usd = local_currency * exchange_rate  

# Step 2: Round the converted amount to 3 decimal places
rounded_amount_before_fees=round(amount_in_usd,3)

# Step 3: Subtract the transaction fee
t=rounded_amount_before_fees- transaction_fee

# Step 4: Round the final amount to 2 decimal places

final_rounded_amount=round(t,2)
# Output the results
print(f"Amount before fees (rounded to 3 decimals): {rounded_amount_before_fees}")
print(f"Final amount after fees (rounded to 2 decimals): {final_rounded_amount}")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB225)