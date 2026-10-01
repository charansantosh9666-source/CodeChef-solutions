# PYTHPROB105

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Favourite Pet Inquiry

In this task, you will create a program that asks the user to describe their dream pet.
The program will gather details such as the type of pet, its name, its color, and the number of pets the user dreams of having.
Additionally, it will calculate what it would be like to have one more than their dream number of pets.

 **Output Format:** 

```
Your dream pet is a <pet_color> <pet_type> named <pet_name>.
You dream of having <number_of_pets> Cat(s), but imagine having <total_pets>! How adorable!

```

 **Note:**  total_pets = number_of_pets + 1

Check the sample output below for further clarity.
Review the comments given in the IDE and complete the code.

### Sample 1:
Input
Output

```
Parrot
Kiwi
Yellow
2
```

```
Your dream pet is a Yellow Parrot named Kiwi.
You dream of having 2 Parrot(s), but imagine having 3! How adorable!
```

### Sample 2:
Input
Output

```
Cat
Whiskers
white
3
```

```
Your dream pet is a white Cat named Whiskers.
You dream of having 3 Cat(s), but imagine having 4! How adorable!
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T04:13:35.691Z  

```py
pet_type=input()
pet_name=input()
pet_color=input()
number_of_pets=int(input())
total_pets=number_of_pets+1

print(f"Your dream pet is a {pet_color} {pet_type} named {pet_name}.") 

print(f"You dream of having {number_of_pets} {pet_type}(s), but imagine having {total_pets}! How adorable!")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB105)