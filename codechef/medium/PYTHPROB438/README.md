# PYTHPROB438

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked Example - Extract Ingredients from a Recipe

In this example, we demonstrate how to use Python’s `split()` method to break a string containing a list of recipe ingredients into a list of individual ingredients. This makes it easier to manage or process them separately.

Consider the following variable:

```
ingredient_list = "flour,sugar,eggs,milk,butter"

```

When the given code is executed, the output will be a list of ingredients:

```
['flour', 'sugar', 'eggs', 'milk', 'butter']

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-25T01:54:46.236Z  

```py
# Define a string containing a list of ingredients separated by commas
ingredient_list = "flour,sugar,eggs,milk,butter"

# Split the string into a list using ", " as the delimiter
ingredients = ingredient_list.split(",")

# Print the resulting list of ingredients
print(ingredients)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB438)