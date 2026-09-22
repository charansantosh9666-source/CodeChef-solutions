# PYTHPROB424

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Document processing system

You are developing a text search feature for a document processing system. The system needs to find the position of a specific word in a given sentence.

Given the following code snippet:

```
text = "The quick brown fox jumps over the lazy dog."
position = text.index("fox")
print(position)

```

 **What will be the output of the program?**

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-22T01:15:27.046Z  

```cpp
# Define a string  
text = "Learning Python is fun and rewarding!"

# Use the index() method to find the starting index of the word "Python"
# Unlike find(), index() raises a ValueError if the substring is not found
position = text.index("Python")

# Print the index where "Python" starts in the string
print(position)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB424)