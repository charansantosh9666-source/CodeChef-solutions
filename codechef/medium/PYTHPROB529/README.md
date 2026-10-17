# PYTHPROB529

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Pet Age Classification

In this task, we will determine a pet's age category based on its age in years. The program will use nested if statements to classify the pet into different groups.

- Puppy → If the age is less than 1
- Young Adult → If the age is 1 to less than 3 years.
- Mature Adult → If the age is 3 to less than 8 years.
- Senior → If the age is 8 years or more.

 **Task** 

- Take the pet’s age as input from the user.
- Convert the user input to an integer data type.
- Print the pet’s age category based on the conditions.
### Sample 1:
Input
Output

```
2
```

```
Young Adult
```

### Sample 2:
Input
Output

```
9
```

```
Senior
```

### Sample 3:
Input
Output

```
0 
```

```
Puppy
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T16:41:30.825Z  

```py
age = int(input( ))  # Convert the input string to an integer

# Check if the pet is a Puppy (less than 1 year old)
if age < 1:
    print("Puppy") 
else:
    
    if age < 3:
        print("Young Adult") 
    elif age < 8:
        print("Mature Adult") 
    
    else:
        print("Senior") 
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB529)