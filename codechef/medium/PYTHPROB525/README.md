# PYTHPROB525

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T01:18:04.267Z  

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

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB525)