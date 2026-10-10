# Step 1: Define Team A's target and Team B's score
team_a_target = int(input())  # Team A's target score
team_b_score = int(input())   # Team B's score

# Step 2: Check if the scores are different using the != operator
if team_b_score != team_a_target:
    print("Team B did not match the target.")  # Output if scores are different
else:
    print("Team B matched the target.")  # Output if scores are the same

