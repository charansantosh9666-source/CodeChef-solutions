# PYTHPROB140

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Favorite City Input Cleanup

In this task, you will create a program that asks the user for their favorite city and how many times they would like to visit it. The program will clean up extra spaces, handle multi-word city names, and display the cleaned input in a friendly message.

 **Output Format:** 

```

Your favorite city is: '<city>', and you want to visit it <visits> times.

```

 **Steps to Complete the Exercise:** 

- Use input() to ask the user for their favorite city and the number of visits, all on one line.
- Use.split() to separate the words in the input.
- Extract the city name and visit count from the split values.
- Use.strip() to clean any extra spaces around the city name.
- Convert the visit count to an integer.
- Print a message with the cleaned city name and visit count.
### Sample 1:
Input
Output

```
NewYork 5

```

```
Your favorite city is: 'NewYork', and you want to visit it 5 times.
```

### Sample 2:
Input
Output

```
Paris 3

```

```
Your favorite city is: 'Paris', and you want to visit it 3 times.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T02:02:31.162Z  

```py
user_input = input() 

city, visits = user_input.split()

city = city.strip()

visits = int(visits.strip())


print(f"Your favorite city is: '{city}', and you want to visit it {visits} times.")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB140)