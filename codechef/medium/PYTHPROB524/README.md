# PYTHPROB524

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Determine Traffic Light Action

In this task, we will create a program that determines what action a driver should take based on the traffic light color. The categorization of actions is as follows:

- If the light is red or flashing red, the action is Stop.
- If the light is yellow or blinking yellow, the action is Slow Down.
- If the light is green or blinking green, the action is Go.
- If the input is not a valid color, the program should print Invalid input.

We will use the if-elif-else structure to determine the appropriate action based on the traffic light color.

 **Task** 

- Take the main traffic light color as input from the user.
- Take user input for the blinking light color and store in variable blinking_light
### Sample 1:
Input
Output

```
green
blinking green
```

```
Go

```

### Sample 2:
Input
Output

```
purple
blinking purple
```

```
Invalid input
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T01:18:01.004Z  

```py
# Take user input for traffic light color and process it
main_light = input( )

# Take user input for blinking light color
blinking_light = input( )

# Check the light color and determine the action using 'or' operator
if main_light == "red" or blinking_light == "flashing red":
    print("Stop")  
elif main_light == "yellow" or blinking_light == "blinking yellow":
    print("Slow Down")  
# Update the code below this line
elif main_light=="green" or blinking_light =="blinking green" :
    print("Go")
else:
    print("Invalid input")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB524)