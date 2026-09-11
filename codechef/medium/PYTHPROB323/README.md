# PYTHPROB323

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked Example - Using Quotes in Strings

This example demonstrates how to work with strings that include both single and double quotes in Python.

You can use different quoting styles or escape characters to ensure that quotes are printed correctly without causing syntax errors.

- By enclosing a string in double quotes, you can easily include single quotes within it: string1 = "Einstein once said, 'Imagination is more important than knowledge.'"
- If you need to use the same type of quote inside the string that you are using for the string delimiter, you can escape it with a backslash \: string2 = 'Einstein once said, \'Imagination is more important than knowledge.\''

When printed, both strings will display as intended:

```
Einstein once said, 'Imagination is more important than knowledge.'
Einstein once said, 'Imagination is more important than knowledge.'

```

This example effectively illustrates how to manage different types of quotes in Python strings.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-11T01:08:24.497Z  

```py
# Step 1: Using double quotes for the outer string and single quotes inside
quote = "Einstein once said, 'Imagination is more important than knowledge.'"

# Step 2: Using escape sequences to handle quotes inside the string
escaped_quote = 'Einstein once said, \'Imagination is more important than knowledge.\''

# Step 3: Print both quotes
print(quote)
print(escaped_quote)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB323)