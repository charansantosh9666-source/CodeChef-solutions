# PYTHPROB130

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Plan Your Weekend - Coding Challenge

In this task, you will create a program to help users plan their weekend activities.
The program will gather details about their favorite activity, place to visit, number of friends, and hours spent.
It will practice handling multiple inputs, using `.split()` for efficient input handling, `map()` for numeric conversions, and `.upper()` for formatting text in uppercase.

 **Output Format:** 

```
You plan to go <favorite_activity> at the <favorite_place>.
You will be joined by <num_friends> friends and will spend <hours_spent> hours there.

```

 **Steps to Complete the Task:** 

- Get the input: Ask the user for their favorite activity and place to visit, then store them using.split().
- Use.upper(): Convert both the activity and place to uppercase.
- Get numeric inputs: Prompt the user to enter the number of friends and hours, then convert these to integers using map(int, input().split()).
- Print the output: Display a summary of the user's weekend plan.
### Sample 1:
Input
Output

```
Cycling Park
2 4
```

```
You plan to go CYCLING at the PARK.
You will be joined by 2 friends and will spend 4 hours there.
```

### Sample 2:
Input
Output

```
Running Track
4 2
```

```
You plan to go RUNNING at the TRACK.
You will be joined by 4 friends and will spend 2 hours there.
```

### Sample 3:
Input
Output

```
Swimming Pool
2 2
```

```
You plan to go SWIMMING at the POOL.
You will be joined by 2 friends and will spend 2 hours there.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T02:03:49.337Z  

```py
activity,place=input().split()

favorite_activity=activity.upper()

favorite_place=place.upper()

num_friends,hours_spent=map(int,input().split())

print(f"You plan to go {favorite_activity} at the {favorite_place}.")
print(f"You will be joined by {num_friends} friends and will spend {hours_spent} hours there.")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB130)