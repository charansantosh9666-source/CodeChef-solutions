# PYTHPROB363C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked Example - Negative Slicing

In this example, we demonstrate how to use negative slicing with a file path string to extract the last 10 characters. Negative slicing allows you to retrieve characters from the end of a string without needing to know its total length in advance.

Consider the following string:

```
file_path = "C:/Users/Admin/Documents/project_report.pdf"

```

When this code is executed, the output will be:

```
_report.pdf

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T08:17:50.901Z  

```py
file_path = "C:/Users/Admin/Documents/project_report.pdf"

# Extract the last 11 characters using negative slicing
last_part = file_path[-11:]

# Print the result
print(last_part)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB363C)