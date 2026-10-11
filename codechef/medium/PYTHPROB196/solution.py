# Prompt the user to input their grade and attendance percentage
a=int(input())
b=int(input())

# Check eligibility based on grade and attend
if a>=75 and b>=75:
    print("Eligible for the school trip.")
else:
    print("Not eligible for the school trip.")
