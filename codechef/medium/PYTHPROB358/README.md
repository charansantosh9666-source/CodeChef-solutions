# PYTHPROB358

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Slicing a Quote for No Content

In this example, we will work with a string containing a famous quote. Our goal is to create two slices from that quote, both of which will result in empty strings. This exercise demonstrates how slices in Python can yield empty results under certain conditions.

Consider the following quote string:

```
quote = "The only limit to our realization of tomorrow is our doubts of today."

```

When both slices are printed, the output will be:

```
"" (first slice) 
"" (second slice)

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-14T01:42:45.241Z  

```py
# Define a quote for slicing  
quote = "The only limit to our realization of tomorrow is our doubts of today."

# Empty slice because start and end indices are the same  
first_empty_slice = quote[15:15]  # No characters are selected when start and end are identical  

# Empty slice because the start index is greater than the end index  
second_empty_slice = quote[20:15]  # Python slicing does not throw an error, but returns an empty string  

# Print the results (both will output an empty string)
print(first_empty_slice)
print(second_empty_slice)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB358)