# PYTHPROB335

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Count Characters in a Hobby Description

In this task, you are required to preserve a multi-line comment as a string and then check how many characters it contains. This will help you practice your understanding of triple-quoted strings and the `len()` function in Python.

You should create a multi-line string using triple quotes (either `"""` or `'''`) that contains the following text:

```
I love gardening.
It allows me to connect with nature and grow my own food.
Every day in the garden is a learning experience.

```

After creating this multi-line text and assigning it to a variable named `comment`, you will use the `len()` function to calculate the total number of characters (including spaces and line breaks) and print the result.

 **Expected Output** 
After performing the calculation, your program should print the length of the string as follows:

```
127

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-11T01:16:03.948Z  

```py
# Assign the multi-line comment to a variable as a string
comment = """
I love gardening.
It allows me to connect with nature and grow my own food.
Every day in the garden is a learning experience.
"""

# Calculate and print the total number of characters in the comment
print(len(comment))
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB335)