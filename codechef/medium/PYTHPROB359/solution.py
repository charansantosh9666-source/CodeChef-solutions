# Define a quote for slicing  
quote = "The only limit to our realization of tomorrow is our doubts of today."

# Empty slice because start and end indices are the same  
first_empty_slice = quote[15:15]  # No characters are selected when start and end are identical  

# Empty slice because the start index is greater than the end index  
second_empty_slice = quote[20:15]  # Python slicing does not throw an error, but returns an empty string  

# Print the results (both will output an empty string)
print(first_empty_slice)
print(second_empty_slice)