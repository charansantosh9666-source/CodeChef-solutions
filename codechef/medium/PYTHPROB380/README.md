# PYTHPROB380

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### My Movie Details

In this task, you are required to standardize various text elements for consistent display, including movie titles, promo messages, and disclaimers.

You will work with the following data:

- "tHe aVENGerS: eNDgAMe" to a variable named movie_title.
- "Don't Miss The Epic Finale!" to promo_message.
- "TERMS AND CONDITIONS APPLY." to disclaimer.

You need to perform the following transformations:

- Convert movie_title to title case (e.g., movie_title.title()).
- Convert promo_message to uppercase (e.g., promo_message.upper()).
- Convert disclaimer to lowercase (e.g., disclaimer.lower()).

Finally, print the standardized texts in that order on separate lines.

 **Expected Output** 
After performing the transformations, your program should print the results as follows:

```
The Avengers: Endgame
DON'T MISS THE EPIC FINALE!
terms and conditions apply.

```

Feel free to change the input strings to see how the output changes!

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T08:41:47.729Z  

```py
# Given Movie Data
movie_title = "tHe aVENGerS: eNDgAMe"
promo_message = "Don't Miss The Epic Finale!"
disclaimer = "TERMS AND CONDITIONS APPLY."

# Formatting the strings
formatted_title=movie_title.title()
formatted_promo=promo_message.upper()
formatted_disclaimer=disclaimer.lower()



# Display the results
print(formatted_title)
print(formatted_promo)
print(formatted_disclaimer)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHPROB380)