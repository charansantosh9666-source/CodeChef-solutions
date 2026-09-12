# PYTHPROB343

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Access Last Three Characters

In this example, we demonstrate accessing specific characters in the string  **"Programming is fun!"**  using negative indexing, an essential technique for string manipulation in Python.

Here’s a breakdown of the characters and their corresponding negative indices in the string  **"Programming is fun!"** :

```
String:       P   r   o   g   r   a   m   m   i   n   g       i   s       f   u   n   !
Index:        0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18
Negative:    -19 -18 -17 -16 -15 -14 -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

```

- The last character is at index -1.
- The second-to-last character is at index -2.
- The third-to-last character is at index -3.

When you access the characters using these negative indices, you get "f", "u", and "n". Therefore, the last three characters of the string are  **"fun"**.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-12T01:13:11.951Z  

```py
# Define the string
string = "Programming is fun!"

# Access the last character using negative index -2
last_char = string[-2]

# Access the second to last character using negative index -3
second_last_char = string[-3]

# Access the third to last character using negative index -4
third_last_char = string[-4]

# Concatenate the last three characters
result = third_last_char + second_last_char + last_char

# Print the result
print(result)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB343)