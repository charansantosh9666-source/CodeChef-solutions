# Step 1: Define Team A's target and Team B's score
team_a_target = int(input())  # Input target score
team_b_score = int(input())   # Input Team B's score

# Step 2: Compare the scores using the == operator
if team_b_score == team_a_target:
    print("The match is tied!")      # Output if scores are equal
else:
    print("The match is not tied!")  # Output if scores are not equal
