# Step 1: Take user input for Team A's target and Team B's score
team_a_target = int(input())  # Input Team A's target score
team_b_score = int(input())          # Input Team B's score

# Step 2: Use if-else to determine the winner
if team_b_score > team_a_target:  # Check if Team B's score is greater than Team A's target
    print("Team B wins!")         # Output if Team B wins
else:
    print("Team A wins!")         # Output if Team A wins
