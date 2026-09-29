# PYTHPROB465

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Center a Birthday Message

You have a birthday message, "Happy Birthday!", and you want to make it look extra special by applying several transformations:

- Convert to uppercase for emphasis.
- Center the message in a 50-character width using '=' as the fill character.
- Replace all spaces with '*'.
### Expected Output

```
=================HAPPY*BIRTHDAY!==================

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-29T02:40:07.941Z  

```py
birthday_message = "Happy*Birthday!"  # Original message

centered_message=birthday_message.center(50,"=")


# Print the final formatted birthday message
print(centered_message)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB465)