# PYTHPROB139

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### MCQ - Handling Whitespace in Input

You are creating a program that asks the user to enter their favorite quote. The program needs to handle input properly by removing any leading or trailing spaces. What will be the output of the following code if the user enters

```

"       Keep moving forward        " 

```

(with extra spaces at the beginning and end)?

```
quote = input()
print(f"Original Quote: '{quote}'")
print(f"After lstrip(): '{quote.lstrip()}'")
print(f"After rstrip(): '{quote.rstrip()}'")
print(f"After strip(): '{quote.strip()}'")

```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T02:06:00.786Z  

```cpp
user_input = input()

leading_cleaned = user_input.lstrip()

trailing_cleaned = user_input.rstrip()

fully_cleaned = user_input.strip()

print(f"Original Address: '{user_input}'")
print(f"After lstrip(): '{leading_cleaned}'")  
print(f"After rstrip(): '{trailing_cleaned}'")  
print(f"After strip(): '{fully_cleaned}'")      
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB139)