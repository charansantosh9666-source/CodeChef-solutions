# PYTHPROB103

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked example - Basic input functions

In this task, you will create a program that asks the user for their favorite hobby, dream travel destination, and how many days they would like to spend there. The program will combine these inputs into an exciting message.

 **Output Format:** 

```

Imagine enjoying your hobby, <favorite_hobby>, while relaxing in <dream_destination>  
for <days_to_spend> days!

```

 **Steps to Complete the Task:** 

- Ask for the user's favorite hobby using input().
- Ask for their dream travel destination using input().
- Ask for how many days they would love to spend using int(input()).
- Store inputs in variables.
- Print a message that combines the collected information into a meaningful sentence.
### Sample 1:
Input
Output

```
Painting
Paris
7

```

```
Imagine enjoying your hobby, Painting, while relaxing in Paris for 7 days!

```

### Sample 2:
Input
Output

```
Skiing
Switzerland
20
```

```
Imagine enjoying your hobby, Skiing, while relaxing in Switzerland for 20 days!
```

### Sample 3:
Input
Output

```
Dancing
Assam
5
```

```
Imagine enjoying your hobby, Dancing, while relaxing in Assam for 5 days!
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T03:22:55.753Z  

```py
# Asks for the user's favorite hobby
favorite_hobby = input()

# Asks for their dream travel destination
dream_destination = input()

# Asks how many days they want to spend there (convert input to an integer)
days_to_spend = int(input())

# Prints a meaningful message using the collected information
print(f"Imagine enjoying your hobby, {favorite_hobby}, while relaxing in {dream_destination} for {days_to_spend} days!")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB103)