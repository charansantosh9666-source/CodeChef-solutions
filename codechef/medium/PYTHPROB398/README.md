# PYTHPROB398

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Trim Trailing Spaces from a Message

In this example, we demonstrate how to use Python’s `rstrip()` method to remove trailing spaces from a message. This ensures that the message does not contain unnecessary whitespace at the end.

Consider the following variable:

```
user_message = "Welcome to the Python course!      "

```

When the given code is executed, the output will be:

```
Welcome to the Python course!

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T09:00:35.761Z  

```py
# Define a string with trailing spaces
user_message = "Welcome to the Python course!      "

# Remove trailing spaces using rstrip()
cleaned_message = user_message.rstrip()

# Print the cleaned message without trailing spaces
print(cleaned_message)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB398)