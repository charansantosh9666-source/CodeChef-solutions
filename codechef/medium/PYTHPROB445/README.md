# PYTHPROB445

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Format a Sentence

You have a sentence in uppercase, "HELLO WORLD".

You want to insert a hyphen ("-") between each character using the join() method, and then test if the result is purely alphabetic using isalpha().

Check the comments given in the IDE and execute your code based on the same.

### Expected Output

```
H-E-L-L-O- -W-O-R-L-D
False

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-27T04:26:44.017Z  

```py
sentence = "HELLO WORLD"  # Given string

f="-".join(sentence)

print(f)

print(f.isalpha())
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB445)