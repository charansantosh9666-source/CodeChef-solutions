# PYTHPROB230

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Distance to the Moon in Scientific Notation

In this task, you are required to create a program to compare distances to two nearby stars, then display both distances and the difference in scientific notation.

You have the following details:

- The first star is 40,150,000,000 kilometers away.
- The second star is 15,750,000,000 kilometers away.

 **Expected Output** 
After performing the calculations, your program should print the results in scientific notation as follows:

```
Distance to Star 1: 4.02e+10 kilometers
Distance to Star 2: 1.58e+10 kilometers
Difference in distances: 2.44e+10 kilometers

```

Feel free to change the distances to see how the outputs change!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T01:40:02.816Z  

```py
# Step 1: Declare the distances to the two stars
distance_star_1 = 40150000000.0  # Distance to the first star in kilometers
distance_star_2 = 15750000000.0  # Distance to the second star in kilometers

# Step 2: Calculate the difference in distances
distance_difference = distance_star_1 - distance_star_2


# Step 3: Update the blanks in the code below
print(f"Distance to Star 1: {distance_star_1:.2e} kilometers")
print(f"Distance to Star 2: {distance_star_2:.2e} kilometers")
print(f"Difference in distances: {distance_difference:.2e} kilometers")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB230)