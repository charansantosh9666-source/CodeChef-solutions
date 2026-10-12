# PYTHPROB519

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Meal Plan Recommendation Based on Age

A nutritionist is designing a meal plan based on a person's age. The program will take a user's age as input and recommend a suitable meal category using the if-elif structure.

 **Task** 

- Take the user's age as input.
- Convert the input to an integer.

 **Use the if-elif structure to determine the meal category** :

- Toddler Meal (0-3 years) → Print Recommended Meal Plan: Toddler Meal
- Kids Meal (4-12 years) → Print Recommended Meal Plan: Kids Meal
- Teen Meal (13-19 years) → Print Recommended Meal Plan: Teen Meal
- Adult Meal (20-59 years) → Print Recommended Meal Plan: Adult Meal

Now it's your turn! Write the code and see how different ages get their perfect meal plan!

### Sample 1:
Input
Output

```
50
```

```
Recommended Meal Plan: Adult Meal
```

### Sample 2:
Input
Output

```
4
```

```
Recommended Meal Plan: Kids Meal
```

### Sample 3:
Input
Output

```
19
```

```
Recommended Meal Plan: Teen Meal
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-12T02:51:35.647Z  

```py
# Take user input for age and convert it to an integer
age = int(input( ))  

# Use if-elif structure to determine the meal category based on age
# If age is 3 or below, recommend a "Toddler Meal"
if age <= 3:  
    print("Recommended Meal Plan: Toddler Meal")

# Else If age is between 4 and 12 (inclusive), recommend a "Kids Meal"
elif age<=12 and age>=4:
    print("Recommended Meal Plan: Kids Meal")

# Else If age is between 13 and 19 (inclusive), recommend a "Teen Meal"
elif age<=19 and age>=13:
    print("Recommended Meal Plan: Teen Meal")

# Else If age is between 20 and 59 (inclusive), recommend an "Adult Meal"
elif age<=59 and age>=20:
    print("Recommended Meal Plan: Adult Meal")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB519)