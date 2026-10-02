# PYTHPROB123

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Favorite Colors and Numbers Collector

In this task, you will create a program that collects the user's favorite color and favorite number in one input line, and then displays the values in a friendly message.

 **Output Format:** 

```
Your favorite color is <favorite_color> and your favorite number is <favorite_number>.

```

 **Steps to Complete the Task:** 

- Use the input() function to ask the user for their favorite color and number on the same line.
- Use the.split() method to separate the input into two parts: the color and the number.
- Print a message that includes the separated values.
### Sample 1:
Input
Output

```
Blue 7
```

```
Your favorite color is Blue and your favorite number is 7.
```

### Sample 2:
Input
Output

```
Red 15
```

```
Your favorite color is Red and your favorite number is 15.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T03:30:15.706Z  

```py
# User enter their favorite color and number
user_input = input()

# Spliting the input into color and number
favorite_color, favorite_number = user_input.split()

# now convert the number to an integer
favorite_number = int(favorite_number)

# print the friendly message
print(f"Your favorite color is {favorite_color} and your favorite number is {favorite_number}.")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB123)