# Step 1: Define the required distance and participant's distance
required_distance =int(input())# User input - Minimum distance required to qualify 
participant_distance =int(input()) # User input - Distance run by the participant 

# Step 2: Check if the participant qualifies for the next round
if participant_distance >= required_distance:  # Is the participant's distance enough to qualify?
    print("Qualified for next round!")  # Print result if the condition is true
