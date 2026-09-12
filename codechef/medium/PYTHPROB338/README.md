# PYTHPROB338

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Accessing Characters in a Greeting

In this example, we demonstrate accessing specific characters in the string "Good Morning!" using positive indices, an essential aspect of string manipulation in Python.

Here’s a breakdown of the characters and their corresponding indices in the string "Good Morning!":

```
String:  G   o   o   d       M   o   r   n   i   n   g   !
Index:   0   1   2   3   4   5   6   7   8   9   10  11  12

```

- The first character is at index 0.
- The fourth character is at index 3.
- The last character is at index 12.

When printed, the output would clearly represent the accessed characters from the string.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-12T01:07:53.071Z  

```py
# Declare a string variable
my_string = "Good Morning!"

# Access the first character using positive indexing
first_character = my_string[0]  # Should give 'G' (the first character of the string)

# Access the fourth character using positive indexing
fourth_character = my_string[3]  # Should give 'd' (the character at index 3)

# Access the last character using positive indexing
last_character = my_string[12]  # Should give '!' (the character at index 12)

# Print the extracted characters
print(first_character)  # Output: G
print(fourth_character)  # Output: d
print(last_character)  # Output: !
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB338)