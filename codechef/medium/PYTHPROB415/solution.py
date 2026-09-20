# Declare the address string
address = "    1234 Elm St. "

# Check if the address contains only alphanumeric characters 

is_alphanumeric=address.isalnum()
# Clean the address by stripping leading and trailing spaces
cleaned_address=address.strip() 

# Print the results
print(is_alphanumeric) 
print(cleaned_address)
