# PYTHPROB223

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked Out Example - Round Weekly Temp Average

In this example, we calculate the average temperature over a week and round that average to two decimal places using Python’s built-in `round()` function.

The process involves gathering daily temperatures for 7 days, summing these temperatures, then dividing the total by 7 to determine the average. Finally, we can use `round(average, 2)` to limit the result to two decimal places.

For instance, consider the daily temperatures:

- Day 1: 22.5
- Day 2: 23.0
- Day 3: 21.75
- Day 4: 24.0
- Day 5: 23.5
- Day 6: 22.0
- Day 7: 21.25

The average temperature can be calculated, and when rounded, the output will reflect the temperature rounded to two decimal places.

This example effectively illustrates how to calculate and round values in Python.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T01:33:17.014Z  

```py
# Step 1: Declare 7 different variables for daily temperatures
day1_temp = 23.5
day2_temp = 24.3
day3_temp = 22.7
day4_temp = 25.1
day5_temp = 21.8
day6_temp = 23.9
day7_temp = 24.2

# Step 2: Calculate the sum of the temperatures
total_temp = day1_temp + day2_temp + day3_temp + day4_temp + day5_temp + day6_temp + day7_temp

# Step 3: Calculate the average temperature
average_temp = total_temp / 7

# Step 4: Round the average temperature to two decimal places
rounded_average_temp = round(average_temp, 2)

# Step 5: Print the rounded average temperature
print(rounded_average_temp)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB223)