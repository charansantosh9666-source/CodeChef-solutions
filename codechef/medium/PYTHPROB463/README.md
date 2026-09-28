# PYTHPROB463

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Center a Custom Greeting Message

In this example, we demonstrate how to use Python’s `center()` method to create a nicely formatted birthday greeting by centering the string "Happy Birthday!" within a width of 30 characters. Additionally, we fill the extra space on both sides with the `#` character for a fun decorative effect.

Consider the following variable:

```
greeting = "Happy Birthday!"

```

When the given code is executed, the output will be the centered greeting:

```
######Happy Birthday!######

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-28T01:54:03.140Z  

```py
# Original greeting message
greeting = "Happy Birthday!"

# Center the greeting within a width of 30 characters, using '#' as padding
centered_greeting = greeting.center(30, '#')

# Print the formatted greeting
print(centered_greeting)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB463)