# Assigning the invoice number as a string
invoice_number = '7'

# Using zfill() to pad the invoice number to a width of 3, filling with leading zeros
formatted_invoice = invoice_number.zfill(3)

# Printing the formatted invoice number
print(formatted_invoice)