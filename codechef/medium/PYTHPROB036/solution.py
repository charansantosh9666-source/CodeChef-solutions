# Initial number of shares on the first day
initial_shares = 10

# Day for which to calculate the number of shares
day = 4 
initial_shares *=pow(3,day)
print(f"On day {day}, the post will be shared by {initial_shares} people.")