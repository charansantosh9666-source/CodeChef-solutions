# PYTHPROB453

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Check File Extension for Image

In this example, we demonstrate how to use Python’s `endswith()` method to check if a file name ends with one of the common image file extensions—".jpg", ".png", or ".gif". This scenario is typical in programs that need to validate file types before processing them.

Consider the following variable:

```
filename = "photo.jpeg"

```

When the given code is executed, the output will be:

```
False

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-27T04:31:25.725Z  

```py
# Define the filename of the image
filename = "photo.jpeg"

# Check if the file has a valid image extension (.jpg, .png, .gif)
is_image = filename.endswith((".jpg", ".png", ".gif"))

# Output the result (True if the file is an image, otherwise False)
print(is_image)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB453)