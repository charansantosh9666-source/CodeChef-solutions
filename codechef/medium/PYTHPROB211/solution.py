# Declare the initial distance as a float
d=float(125.5)
# Declare the distance traveled on day 1 as an integer
d1=50
# Declare the distance traveled on day 2 as a float
d2=float(78.25)
# Declare the error correction as an integer
e=12

# Declare the calibration adjustment as a float
c=float(5.75)

# Calculate the total distance traveled
total_distance=d+d1+d2-e-c


# Print the total distance traveled
print(total_distance)  