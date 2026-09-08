# PYTHPROB224

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Calculate The Product Price

A store is selling a product at a price of `$7.5678`. The store wants to round the price to two decimal places for convenience in billing. The store uses the `round()` function to round the price.

What will the final price be displayed to the customer after rounding?

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T01:33:55.097Z  

```cpp
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

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB224)