# PYTHPROB353

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Copy a Greeting Message

In this example, we will learn how to make a copy of an entire string by using a full string slice. This technique can be particularly useful when you need to duplicate or modify strings without altering the original.

Consider the following greeting string:

```
greeting = "Welcome to Python Programming!"

```

To create a copy of this string, we can use the full string slice `[:]`, which creates a new string that is a duplicate of the original.

We can assign the copied string to a new variable called  **greeting_copy**.

When the copy is printed, the output will appear as follows:

```
Welcome to Python Programming!

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T08:14:40.653Z  

```py
# Assigning a string to the variable 'greeting'
greeting = "Welcome to Python Programming!"

# Creating a copy of the 'greeting' string using slicing
greeting_copy = greeting[:]

# Printing the copied string
print(greeting_copy)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB353)