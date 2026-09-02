# PYTHPROB020

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### My Total Income

In this task, you are required to calculate your total weekly income based on three part-time jobs, each with its own hourly rate and the number of hours worked per week. Your program should display the total weekly income after performing the calculations.

 **Hourly Rates** 

- Job 1: $20/hour
- Job 2: $15/hour
- Job 3: $25/hour

 **Weekly Hours** 

- Job 1: 10 hours
- Job 2: 8 hours
- Job 3: 12 hours

 **Expected Output** 
After performing the calculations, your program should print the total weekly income:

```
620

```

Feel free to adjust the rates and hours to see how your total weekly income changes!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-02T11:57:05.647Z  

```py
# Hourly rates for three part-time jobs (in dollars)
job1_rate = 20
job2_rate = 15
job3_rate = 25

# Hours worked in a week for each job
job1_hours = 10
job2_hours = 8
job3_hours = 12

# Update your code below this line
total=(job1_hours * job1_rate)+(job2_hours * job2_rate)+(job3_hours* job3_rate)
print(total)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB020)