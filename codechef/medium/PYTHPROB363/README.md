# PYTHPROB363

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Getting a Substring from a Name

In this example, we demonstrate how to extract a person's first name from a full name string using Python's string slicing.

To isolate the first name, we determine the position of the space character, which separates the first name from the last name. For instance, in the string `"John Doe"`, the first name "John" spans indices [0:4]. The space character at index 4 indicates where the first name ends.

When running the code with this example, the output would be:

```
John

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-14T01:43:59.907Z  

```py
# Assigning the full name to the variable
full_name = "John Doe"

# Extracting the first name (first 4 characters of the full name)
first_name = full_name[0:4]

# Printing the extracted first name
print(first_name)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB363)