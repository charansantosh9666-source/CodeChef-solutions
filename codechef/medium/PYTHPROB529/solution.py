age = int(input( ))  # Convert the input string to an integer

# Check if the pet is a Puppy (less than 1 year old)
if age < 1:
    print("Puppy") 
else:
    
    if age < 3:
        print("Young Adult") 
    elif age < 8:
        print("Mature Adult") 
    
    else:
        print("Senior") 