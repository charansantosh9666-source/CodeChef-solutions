# PYTHPROB365

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### A Task on Slice vs Index

In this task, you are required to retrieve a single character from a specific index and a substring using slicing from a given string. This will demonstrate the difference between indexing (fetching one item) and slicing (retrieving a range).

You should use the following string:

```
text = "PythonProgramming"

```

You need to perform the following:

- Extract the 5th character of text (remember indexing starts at 0) and store it in a variable named char_at_index.
- Extract the first 6 characters of text using slicing and store them in a variable named slice_text.
- Print both char_at_index and slice_text in a descriptive format.

 **Expected Output** 
After performing the calculations, your program should print the results as follows:

```
Character at index 4: o
First 6 characters: Python

```

Feel free to change the string to see how the outputs vary!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T08:15:51.925Z  

```py
# Define the string
text = "PythonProgramming"

# Extract the 5th character using indexing

char_at_index=text[4]
# Extract the first 6 characters using slicing
slice_text=text[:6]

# Print the results
print("Character at index 4:", char_at_index)
print("First 6 characters:", slice_text)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB365)