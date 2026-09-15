# PYTHPROB364

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Extract Last Name from Full Name

You have a string representing a full name, "Jane Smith". Your goal is to extract only the last name using string slicing.

 **Expected Output** 
If the variable full_name were "Jack Jonny", the program should display:

```
Jonny

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T01:11:29.618Z  

```py
# Assigning the full name to the variable
full_name = "Jane Smith"

# Slicing the string to get the last name (from index 5 onwards)
name=full_name[5:]
# Printing the extracted last name
print(name)

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB364)