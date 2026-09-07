# PYTHPROB220

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Average Temperature Calculation

In this task, you are required to create a program that calculates the average temperature for a week using float division. You have the following daily temperatures in Celsius:

- Day 1: 22.5
- Day 2: 24.0
- Day 3: 19.8
- Day 4: 23.4
- Day 5: 20.1
- Day 6: 25.0
- Day 7: 21.7

 **Expected Output** 
After performing the calculations for the average temperature, your program should print the results in the following format:

```
The average temperature for the week is: 22.357142857142854

```

Feel free to adjust the daily temperatures to see how the average changes!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-07T01:28:19.316Z  

```py
# Step 1: Define the temperatures for each day of the week (in degrees Celsius)
day1 = 22.5
day2 = 24.0
day3 = 19.8
day4 = 23.4
day5 = 20.1
day6 = 25.0
day7 = 21.7

total=(day1+day7+day2+day3+day4+day5+day6)/7
print(f"The average temperature for the week is: {total}")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB220)