# PYTHPROB455

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Check if a filename ends with txt

You have a file name, "document-report.TXT." You need to check the following

- whether it ends with ".txt" in a case-insensitive manner (i.e., ".TXT" should also be considered valid).
- You also want to convert the entire file name to title case for consistent formatting.

Print the file name after converting it to title case.

Print true or false to indicate whether it ends with ".txt."

### Expected Output

```
Document-Report.Txt
True

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-27T04:34:10.055Z  

```py
# Declare a string with a file name
file_name = "document-report.TXT"

# Convert the file name to title case
print(file_name.title())

file_name=file_name.lower()

print(file_name.endswith(".txt"))


```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB455)