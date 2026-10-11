# Define the age of the user
age = int(input()) 

# Define if the user is an active member
is_active_member = input() 

# Check if the user is eligible based on age and membership status

if age>=18 and age<=50 or is_active_member ==True:
    print("Access granted")
else:
    print("Access denied")