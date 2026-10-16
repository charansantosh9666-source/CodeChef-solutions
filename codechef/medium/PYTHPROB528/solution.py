# Take user input for age and convert it to an integer
age = int(input( ))

# Check if the person qualifies for a child ticket
if age < 13:
    print("Child Ticket: $5")

# If not a child, check if the person qualifies for a senior ticket
else:
    if age >= 65:
        print("Senior Ticket: $7")
    
    # If not a senior, the person is an adult (13 to 64 years old)
    else:
        # Ask if they are a member
        membership = input( )
        
        # Check membership status using a nested if
        if membership == "yes":
            print("Adult Member Ticket: $10")
        else:
            print("Adult Non-Member Ticket: $12")
