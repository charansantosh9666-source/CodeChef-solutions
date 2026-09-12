# PYTHPROB339

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Extracting Characters from a Weather Update

In this task, you are required to retrieve specific characters by their position (index) within a given string.

You have the following string:

```
weather_update = "Today's weather is sunny!"

```

You need to retrieve the characters at the following index positions:

- The second character (index 1).
- The sixth character (index 5).
- The second-to-last character (index len(weather_update) - 2).

 **Expected Output** 
After performing the calculations, your program should print the results as follows:

```
o
'
y

```

Feel free to change the string and observe how the outputs vary!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-12T01:09:10.607Z  

```py
# Declare a string variable for the weather update
weather_update = "Today's weather is sunny!"

# Access and print the second character using positive indexing
print(weather_update[1])
# Access and print the sixth character using positive indexing
print(weather_update[5])
# Access and print the second-to-last character using positive indexing
print(weather_update[-2])
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB339)