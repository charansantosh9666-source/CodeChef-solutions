# PYTHPROB200

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Can a Player Enter a Game

A player is allowed to enter a game if they meet at least one of the following conditions:

- They are 15 years or older.
- They have a valid membership card.

Your task is to write a program that checks whether a player meets either of these conditions. If the player is 15 or older or has a valid membership card, they are allowed to enter. Otherwise, they cannot play.

Take the required inputs from the user.

 **Note:**  When you accept the string input from the user - remember that all forms of YES, yes, YeS, yEs are to be treated as valid.

### Sample 1:
Input
Output

```
16 
No

```

```
You can enter the game!
```

### Sample 2:
Input
Output

```
12
YeS

```

```
You can enter the game!
```

### Sample 3:
Input
Output

```
14
nO
```

```
You cannot enter the game.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T02:24:59.166Z  

```py
age = int(input( ))  
m = input( )  

# Check if the student meets at least one condition

if age>=15 or m=="yes":
    print("You can enter the game!")
else:
    print("You cannot enter the game.")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB200)