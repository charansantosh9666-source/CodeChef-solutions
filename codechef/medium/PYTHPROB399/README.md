# PYTHPROB399

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Cleaning Up a Reminder Note

In this task, you are required to remove unwanted trailing characters from a reminder note using the `rstrip()` method.

You have the following details:

`reminder_note`= `"Buy groceries for the week!------"`.

 **Expected Output** 
After performing the above steps, your program should print the result as follows:

```
Buy groceries for the week!

```

Feel free to change the value of `reminder_note` and observe how the output updates!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T09:03:37.112Z  

```py
# Define the reminder note with unwanted trailing dashes
reminder_note = "Buy groceries for the week!------"

c=reminder_note.rstrip('-')
print(c)

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB399)