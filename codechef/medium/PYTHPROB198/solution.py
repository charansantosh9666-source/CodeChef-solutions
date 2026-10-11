# Predefined variable for the number of hours worked by the employee
completed_hours = 38  # Number of hours worked by the employee

# Predefined variable for the number of meetings attended by the employee
attended_meetings = 6  # Number of meetings the employee has attended

# Check if the employee qualifies for the bonus by verifying if any of the conditions are met:
# 1. If the employee has worked 40 or more hours.
# 2. Or if the employee has attended 5 or more meetings.
if completed_hours >= 40 or attended_meetings >= 5:
    # If either condition is true, print that the employee is eligible for the bonus
    print("Employee is eligible for the bonus.")
else:
    # If neither condition is met, print that the employee is not eligible for the bonus
    print("Employee is not eligible for the bonus.")
