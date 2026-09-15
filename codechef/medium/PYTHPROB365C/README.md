# PYTHPROB365C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Extract File Extension Using Negative Slicing

You have a filename, for instance `"presentation.pptx"`. You need to extract the file extension by using negative slicing and also determine the filename’s length with the len() function.

 **Steps to Complete** 

- Create a variable filename and assign it the string "presentation.pptx".
- Use negative slicing (e.g., filename[-5:]) to extract the extension, then store it in a variable named extension.
- Use the len() function on filename to find its length, and store this in a variable named length.
- Print both length and extension in a descriptive format.

 **Expected output** 

```
Filename Length: 17
File extension:.pptx

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T08:20:27.371Z  

```py
# Step 1: Declare the filename
filename = "presentation.pptx"

# Step 2: Use negative slicing to extract the file extension

extension=filename[-5:]
# Step 3: Find the length of the filename

length=len(filename)
# Step 4: Print the results
print(f"Filename Length: {length}")
print(f"File extension: {extension}")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB365C)