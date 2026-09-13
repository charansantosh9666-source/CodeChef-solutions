# PYTHPROB348

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### The Error in Product Details

In this example, we demonstrate how to fix the spelling of a product name in an e-commerce platform. One of the products is mistakenly labeled as  **"Sea"**  when it should be  **"Tea."** 

To correct the spelling, we will create a new string where we change the first letter of the string from "S" to "T" and then combine it with a descriptive phrase.

Consider the following product name string:

```
object_name = "Sea"

```

To modify the name, we replace the first character "S" with "T", resulting in  **"Tea."** 

Finally, we concatenate the modified name with the detail string  **"is soo tasty."** 

When completed, the output will appear as follows:

```
Tea is soo tasty

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T08:06:58.678Z  

```py
# Step 1: Define the strings
object_name = "Sea"
detail = "is soo tasty"

# Step 2: Change the first letter of 'object' from 'S' to 'T'
modified_object = "T" + object_name[1] + object_name[2]

# Step 3: Concatenate the modified object with detail
updated_description = modified_object + " " + detail

# Step 4: Print the updated description
print(updated_description)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB348)