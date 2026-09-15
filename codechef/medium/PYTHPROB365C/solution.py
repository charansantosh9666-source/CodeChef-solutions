# Step 1: Declare the filename
filename = "presentation.pptx"

# Step 2: Use negative slicing to extract the file extension

extension=filename[-5:]
# Step 3: Find the length of the filename

length=len(filename)
# Step 4: Print the results
print(f"Filename Length: {length}")
print(f"File extension: {extension}")