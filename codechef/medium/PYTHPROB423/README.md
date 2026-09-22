# PYTHPROB423

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Find Position of a Word

In this example, we demonstrate how to use Python’s `index()` method to find the position of the word "Python" in the string "Learning Python is fun and rewarding!" Unlike the `find()` method, the `index()` method will raise an error if the substring is not found, rather than returning -1.

Consider the following variable:

```
sentence = "Learning Python is fun and rewarding!"

```

When the given code is executed, you will see the index where "Python" starts. For the given sentence, the substring "Python" begins at index 9, so you will see:

```
9

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-22T01:14:58.708Z  

```py
# Define a string  
text = "Learning Python is fun and rewarding!"

# Use the index() method to find the starting index of the word "Python"
# Unlike find(), index() raises a ValueError if the substring is not found
position = text.index("Python")

# Print the index where "Python" starts in the string
print(position)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB423)