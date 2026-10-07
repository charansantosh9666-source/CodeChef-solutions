# PYTHPROB138

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Clean Up Your Name Input

In this task, you will create a program that asks the user for their address and removes any extra spaces at the beginning, end, or both. This ensures the address is processed correctly without unwanted whitespace.

 **Output Format:** 

```

Original Address: '   <user_input>   '  
After lstrip(): '<leading_cleaned>   '  
After rstrip(): '   <trailing_cleaned>'  
After strip(): '<fully_cleaned>'  

```

 **Steps to Complete the Exercise:** 

- Use input() to ask the user for their address.
- Apply.lstrip() to remove leading spaces.
- Apply.rstrip() to remove trailing spaces.
- Use `.strip() to remove spaces from both ends.
- Print the cleaned address in a friendly message.
### Sample 1:
Input
Output

```
           123 Main Street   
```

```
Original Address: '   123 Main Street   '
After lstrip(): '123 Main Street   '
After rstrip(): '   123 Main Street'
After strip(): '123 Main Street'
```

### Sample 2:
Input
Output

```
      221B Baker Street     
```

```
Original Address: '      221B Baker Street     '
After lstrip(): '221B Baker Street     '
After rstrip(): '      221B Baker Street'
After strip(): '221B Baker Street'
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T02:05:30.999Z  

```py
user_input = input()

leading_cleaned = user_input.lstrip()

trailing_cleaned = user_input.rstrip()

fully_cleaned = user_input.strip()

print(f"Original Address: '{user_input}'")
print(f"After lstrip(): '{leading_cleaned}'")  
print(f"After rstrip(): '{trailing_cleaned}'")  
print(f"After strip(): '{fully_cleaned}'")      
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB138)