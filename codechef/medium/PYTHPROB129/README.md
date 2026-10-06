# PYTHPROB129

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Dream Car and Year Collection

In this task, you will create a program to collect information about the user's dream car brand, model, and the year they would like to own it. This will help practice gathering input using `.split()` and converting the year using `int()`.

 **Output Format:** 

```

You dream of owning a <car_brand> <car_model> in the year <dream_year>.

```

 **Steps to Complete the Task:** 

- Use the input() function to ask for the car's brand and model on the same line, storing the values with.split().
- Prompt for the desired year, converting the input to an integer using int().
- Print a message summarizing the dream car details.
### Sample 1:
Input
Output

```
Tesla ModelX
2030
```

```
You dream of owning a Tesla ModelX in the year 2030.
```

### Sample 2:
Input
Output

```
Maruti 800
2001
```

```
You dream of owning a Maruti 800 in the year 2001.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-06T01:59:14.567Z  

```py
# User enters their dream car brand and model (same line)
car_brand, car_model =input().split()        # Splitting string inputs

# User enters the year they want to own the car (new line)
dream_year =int(input())                    # Convert input to integer

# Output the collected information
print(f"You dream of owning a {car_brand} {car_model} in the year {dream_year}.")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB129)