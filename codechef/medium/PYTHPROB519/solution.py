# Take user input for age and convert it to an integer
age = int(input( ))

# Check the age group using if-elif structure
if age <= 12:
    # If age is 12 or below, print child ticket price
    print("Child Ticket: $5")
elif age <= 19:
    # If age is between 13 and 19, print teen ticket price
    print("Teen Ticket: $8")
elif age <= 64:
    # If age is between 20 and 64, print adult ticket price
    print("Adult Ticket: $12")
