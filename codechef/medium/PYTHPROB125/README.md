# PYTHPROB125

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Favorite Book and Pages Read

In this task, you will create a program to collect the user's favorite book title and the number of pages read. The program will format the title to lowercase and display a friendly message.

 **Output Format:** 

```
You have read <pages_read> pages of <book_title>.

```

 **Steps to Complete the Task:** 

- Use the input() function to get the book title and pages read, all on one line.
- Use.split() to separate the book title and pages read.
- Format the book title by converting it to lowercase using.lower().
- Print the formatted message showing the number of pages and the formatted book title.
### Sample 1:
Input
Output

```
HarryPotter 120
```

```
You have read 120 pages of harrypotter.
```

### Sample 2:
Input
Output

```
TheGreatGatsby 90
```

```
You have read 90 pages of thegreatgatsby.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T11:56:14.576Z  

```py
user_input = input()

book_title, pages_read = user_input.split()

book_title = book_title.lower()

print(f"You have read {pages_read} pages of {book_title}.")

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB125)