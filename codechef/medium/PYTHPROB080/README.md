# PYTHPROB080

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Daily Routine Reminder

In this task, you are required to write a program that displays your daily routine, divided into morning, afternoon, and evening parts. Each task should appear on a new line, and you will use an empty line to separate different parts of the day. Additionally, utilize the `end` parameter to print items on new lines.

You should format your output as follows:

 **Expected Output** 

```
Morning Routine:
Wake up
Brush teeth
Have breakfast

Afternoon Routine:
Work/Study
Lunch
Nap

Evening Routine:
Exercise
Dinner
Relax/Leisure time

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-31T13:10:29.543Z  

```py
# Printing Morning Routine
print("Morning Routine:")
print("Wake up", end="\n")       # Print the task "Wake up" 
print("Brush teeth", end="\n")   # Print the task "Brush teeth"
print("Have breakfast", end="\n")# Print the task "Have breakfast"

print() # Print an empty line to separate the routines

# Printing Afternoon Routine
print("Afternoon Routine:")
print("Work/Study", end="\n")    # Print the task "Work/Study"
print("Lunch", end="\n")         # Print the task "Lunch"
print("Nap", end="\n")           # Print the task "Nap"

print() # Print an empty line to separate the routines

# Printing Evening Routine
print("Evening Routine:")
print("Exercise", end="\n")    
print("Dinner", end="\n")         
print("Relax/Leisure time", end="\n")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB080)