# PYTHPROB165

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Simple Login Authentication System

In this task, you will create a simple login system for a website.
The goal is to check if the username entered by the user matches the stored username.
To prevent errors caused by extra spaces in the input, your program will remove any leading or trailing spaces before making the comparison.

 **Requirements:** 

- Prompt the user to input their username and store it in a variable called entered_username.
- Use the.strip() method to remove any extra spaces from the entered_username input before comparison.
- Use the == operator to compare stored_username and entered_username: If the entered username matches the stored username, the program should print: "Login Successful". If it does not match, the program should print: "Login Failed".
### Sample 1:
Input
Output

```
admin
```

```
Login Successful
```

### Sample 2:
Input
Output

```
Notadmin
```

```
Login Failed
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T03:31:41.656Z  

```py
# Step 1: Define the stored username
stored_username = "admin"  # The correct username

name=input()
if name==stored_username:
    print("Login Successful")
    
else:
    print("Login Failed")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB165)