# Take user input for age and parental consent
age = int(input( ))  # User inputs age
has_parental_consent = input( )  # User inputs yes or no

# Check if the student meets at least one condition

if age>=13 or has_parental_consent=="yes":
    print("Entry Allowed")
else:
    print("Entry Denied")