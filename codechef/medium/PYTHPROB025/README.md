# PYTHPROB025

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Make the car park

In this task, you are required to calculate how many complete rows of cars can fit in a parking lot and how many cars are left over. You'll use integer division (`//`) and subtraction (`-`) to determine:

- How many rows are completely filled.
- How many cars remain that do not fill a row.

 **Data Values** 

- total_cars = 23
- cars_per_row = 5

 **Expected Output** 
After performing the calculations, your program should print the results as follows:

```
4
3

```

This indicates that there are 4 full rows of cars and 3 leftover cars. Feel free to adjust the total number of cars and cars per row to see how the results change!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T02:02:39.729Z  

```py
# Define the total number of cars and cars per row
total_cars = 23
cars_per_row = 5

# Calculate the number of full rows using integer division (//)
n=23//5
# Calculate the remaining cars using subtraction
a=n-1
# Print the results
print(n,a)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB025)