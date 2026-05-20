# Task 2: Cricket Stats Analysis
# ● Objective: Write a script to analyze cricket stats for a team.
# ● Hints:
# ○ Prompt the user to input the runs scored by each of the five players in a
# cricket match.
# ○ For each player (Player 1 to Player 5) ask the user to input the runs they
# scored.
# ○ Calculate the total runs scored by all players and the average runs.
# ○ Display the total runs and average runs to the user.
# Initialize variables to store total runs and player count

total_run=0
average_run=0
for i in range (1,6):
        run=int(input(F"Enter the the run scored by player {i}: "))
        total_run+=run
        average_run=total_run/5
print("Total Run of Five Player",total_run, "Average Run of Five Player",average_run) 
