# PYTHPROB430

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Count Occurrences in a Review

You have a product review system that analyzes how often a particular keyword appears.
You also want to standardize the review text by converting it to lowercase before counting.

Your goal is to determine how many times "phone" appears and the total length of the review.

### Expected Output

```
this phone is amazing! the camera of this phone is great. i love this phone.
3
76

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-24T01:41:51.951Z  

```py
# Declare the product review
review = "This phone is amazing! The camera of this phone is great. I love this phone."

print(review.lower())

Count=review.count("phone")

print(Count)

print(len(review))

```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB430)