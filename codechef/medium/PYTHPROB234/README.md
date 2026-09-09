# PYTHPROB234

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Scientific Value Difference and Precision

In this task, you are required to round a length measurement to a specific number of decimal places and then calculate the difference due to rounding.

You have the following details:

- The original length is 7.123456789 mm.
- You want to round it to 4 decimal places.

 **Expected Output** 
After performing the rounding and calculations, your program should print the results as follows:

```
Rounded length: 7.1235
Difference in precision: -0.0000

```

Feel free to change the original length or the number of decimal places to see how the results vary!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-09T01:18:29.492Z  

```py
# Step 1: Original length in millimeters
original_length = 7.123456789

# Step 2: Round the value to 4 decimal places
rounded_length = round(original_length,4)

# Step 3: Calculate the difference in precision
precision_difference = original_length - rounded_length
# Step 4: Update the blanks in the code below
print(f"Rounded length: {rounded_length}")
print(f"Difference in precision: {precision_difference:.4f}")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB234)