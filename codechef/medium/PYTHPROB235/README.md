# PYTHPROB235

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### The Temperature Average

In this task, you are required to process three temperature readings by rounding them to 3 decimal places, then compute their average and determine how much this rounding impacts the overall average.

The initial readings (in Celsius) are:

- Temperature 1: 23.87654321
- Temperature 2: 23.8760
- Temperature 3: 23.8769

After rounding, you will find the average of the original readings and the average of the rounded readings. You will also calculate the difference between the original average and the rounded average, rounding this difference to 3 decimal places.

 **Expected Output** 
After performing the calculations, your program should print the results as follows:

```
Rounded Temperature 1: 23.877°C
Rounded Temperature 2: 23.876°C
Rounded Temperature 3: 23.877°C
Average Temperature: [calculated_average]°C
Difference in Average Temperature: [difference]°C

```

Feel free to replace the initial temperature values and observe how the rounded readings, averages, and differences change!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-11T01:07:36.396Z  

```py
# Step 1: Original temperature readings
temperature_1 = 23.87654321
temperature_2 = 23.8760
temperature_3 = 23.8769

# Step 2: Round the values to 3 decimal places
reading_1=round(temperature_1,3)
reading_2=round(temperature_2,3)
reading_3=round(temperature_3,3)



# Step 3: Calculate the average of the rounded temperatures
average_rounded=(reading_1+reading_2+reading_3)/3

# Step 4: Calculate the difference in average temperatures
original_avg = (temperature_1 + temperature_2 + temperature_3) / 3
average_difference = original_avg - average_rounded



# Step 5: Print the results
print(f"Rounded Temperature 1: {reading_1}°C")
print(f"Rounded Temperature 2: {reading_2}°C")
print(f"Rounded Temperature 3: {reading_3}°C")
print(f"Average Temperature: {average_rounded}°C")
print(f"Difference in Average Temperature: {average_difference:.3f}°C")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB235)