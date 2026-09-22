# Define a string  
text = "Learning Python is fun and rewarding!"

# Use the index() method to find the starting index of the word "Python"
# Unlike find(), index() raises a ValueError if the substring is not found
position = text.index("Python")

# Print the index where "Python" starts in the string
print(position)