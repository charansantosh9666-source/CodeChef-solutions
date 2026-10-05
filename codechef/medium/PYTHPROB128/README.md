# PYTHPROB128

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Dream Vacation Planner

In this task, you will create a program that collects details about the user's dream vacation: destination, preferred season, number of companions, and trip duration. The program will output a summary of the vacation plan.

 **Output Format:** 

```
You are planning a trip to <destination> during <season>.
You will be traveling with <companions> companions for <duration> days.

```

 **Steps to Complete the Task:** 

- Use the input() function to ask for the destination and season, storing them using.split().
- Prompt for the number of companions and duration on a new line, converting them into integers with map(int, input().split()).
- Print the vacation summary with the collected information.
### Sample 1:
Input
Output

```
Paris Summer
3 7
```

```
You are planning a trip to Paris during Summer.
You will be travelling with 3 companions for 7 days.
```

### Sample 2:
Input
Output

```
Assam Spring
5 20
```

```
You are planning a trip to Assam during Spring.
You will be travelling with 5 companions for 20 days.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T11:57:19.864Z  

```py
# Collecting user's dream vacation destination and preferred travel season (same line)
destination, season = input().split()  # Splitting string inputs

# Collecting the number of travel companions and estimated trip duration (same line)
companions, duration = map(int, input().split())  # Splitting and converting numeric inputs

# Output the collected information
print(f"You are planning a trip to {destination} during {season}.")
print(f"You will be travelling with {companions} companions for {duration} days.")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB128)