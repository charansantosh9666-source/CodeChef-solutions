# PYTHPROB418

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Find Your Favorite Food in a Sentence

In this example, we demonstrate how to use Python’s `find()` method to locate the starting index of a specific food item ("tacos") in the sentence "I love to eat pizza, tacos, and sushi." This method helps you search for a substring within a larger string, returning the index where it first appears or `-1` if it’s not found.

Consider the following variable:

```
sentence = "I love to eat pizza, tacos, and sushi."

```

When the given code is executed, Python will display the starting index of "tacos" in the sentence. For the given sentence, the substring "tacos" starts at index 21, so you will see:

```
21

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-21T16:31:07.523Z  

```py
# Define a string
text = "I love to eat pizza, tacos, and sushi."

# Find the index of the word "tacos" in the string
# The find() method returns the starting index of the first occurrence of "tacos", or -1 if not found.
position = text.find("tacos")

# Output the index where "tacos" is found
print(position)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB418)