# PYTHPROB210

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### My Weekly Health Data

In this task, you are required to write a program to calculate the total distance traveled by a vehicle, using both integer and float values.

 **Data Values** 

- The initial distance traveled is 125.5 km (float).
- On day 1, an extra 50 km is added (integer).
- On day 2, an additional 78.25 km is added (float).
- You then subtract 12 km for an error correction (integer).
- Lastly, you subtract 5.75 km for a calibration adjustment (float).

 **Expected Output** 
After performing the calculations for the distances traveled, your program should print the total distance as follows:

```
236.0

```

Feel free to change the distance values and see how the total distance updates!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-06T02:22:09.085Z  

```py
# Declare the initial distance as a float
d=float(125.5)
# Declare the distance traveled on day 1 as an integer
d1=50
# Declare the distance traveled on day 2 as a float
d2=float(78.25)
# Declare the error correction as an integer
e=12

# Declare the calibration adjustment as a float
c=float(5.75)

# Calculate the total distance traveled
total_distance=d+d1+d2-e-c


# Print the total distance traveled
print(total_distance)  
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB210)