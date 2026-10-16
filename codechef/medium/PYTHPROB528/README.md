# PYTHPROB528

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Worked out Example - Movie Ticket Pricing

A cinema charges different ticket prices based on age and membership status. Your task is to determine the ticket price using nested if statements.

 **Ticket Categories:** 

- Child Ticket (Ages 0 to 12) → $5
- Senior Ticket (Ages 65 and above) →$7
- Adult Ticket (Ages 13 and above) →
- Member Price → $10,
- Non-Member Price → $12

 **Logic & Code Flow** 

- Take age as input and convert it to an integer.
- If age is 0-12, print Child Ticket: $5.
- Else, if age is 65 or above, print Senior Ticket: $7.
- Else (age 13-64):
- Ask for membership status (yes or no).
- If yes, print Adult Member Ticket: $10.
- If no, print Adult Non-Member Ticket: $12.
- Display the final ticket price based on the classification.
### Sample 1:
Input
Output

```
20
yes
```

```
Adult Ticket: $10
```

### Sample 2:
Input
Output

```
10

```

```
Child Ticket: $5
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-16T03:33:29.992Z  

```py
# Take user input for age and convert it to an integer
age = int(input( ))

# Check if the person qualifies for a child ticket
if age < 13:
    print("Child Ticket: $5")

# If not a child, check if the person qualifies for a senior ticket
else:
    if age >= 65:
        print("Senior Ticket: $7")
    
    # If not a senior, the person is an adult (13 to 64 years old)
    else:
        # Ask if they are a member
        membership = input( )
        
        # Check membership status using a nested if
        if membership == "yes":
            print("Adult Member Ticket: $10")
        else:
            print("Adult Non-Member Ticket: $12")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB528)