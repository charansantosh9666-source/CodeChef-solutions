# PYTHPROB229

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Converting Distance for Space exploration

A spacecraft is traveling to a distant star. The distance to the star is approximately `1,234,567,890` kilometers. As part of a report, this distance must be expressed in scientific notation with 2 decimal places.

What will the following Python code output for the distance?

```
distance = 1234567890.0
print(f"{distance:.2e} kilometers")

```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T01:38:52.317Z  

```cpp
# Define the numbers
large_number = 9876543210000000.0
small_number = 0.000000012345

# Convert the numbers to scientific notation with 3 decimal places
large_number_scientific = f"{large_number:.3e}"
small_number_scientific = f"{small_number:.3e}"

# Print the results with meaningful labels
print(f"Large number in scientific notation: {large_number_scientific}")
print(f"Small number in scientific notation: {small_number_scientific}")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB229)