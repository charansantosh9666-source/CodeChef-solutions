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