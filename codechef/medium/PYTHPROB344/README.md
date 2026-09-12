# PYTHPROB344

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Extract Last Four Letters of a Phrase

You have a string: "Learning Python is exciting!" and want to retrieve its last four characters using negative indices.

Negative indexing in Python starts from the end of the string, with -1 referring to the last character.

 **Expected Output** 

```
ing!

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-12T01:14:55.481Z  

```py
# Define the string
string = "Learning Python is exciting!"

# Access the last character using negative index -1
last_char=string[-1]

# Access the second to last character using negative index -2
second_last_char=string[-2]

# Access the third to last character using negative index -3
third_last_char=string[-3]

# Access the fourth to last character using negative index -4

fourth_last_char=string[-4]
# Concatenate the last four characters
result = fourth_last_char + third_last_char + second_last_char + last_char

# Print the result
print(result)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB344)