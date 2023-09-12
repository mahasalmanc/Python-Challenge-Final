import os
import csv

total_votes = 0
unique_candidates = set()
candidate_percentage = {}
candidate_votes = {}

csvpath = "PyPoll/Resources/election_data.csv"

with open(csvpath) as csvfile:
    voting_data = csv.reader(csvfile, delimiter= ",")
    print(voting_data)

    header = next(voting_data)

    for r in voting_data:
        total_votes +=1
        candidates = r[2]
        unique_candidates.add(candidates)
        if candidates in candidate_votes:
            candidate_votes[candidates] +=1

        else:
            candidate_votes[candidates] = 1
    

    print(candidate_votes)
    candidate_list = [c for c in unique_candidates]
    for candidate,count in candidate_votes.items():
        candidate_percentage[candidate]=(count/total_votes)*100
    

    print(candidate_percentage)
    
winner = max(candidate_votes,key=candidate_votes.get)
print(f"The winner is {winner}")
percentage_list = list(candidate_percentage.items())
print(percentage_list[1])
print(f"The total number of votes cast in the election was {total_votes}")
print(f"The candidates running consist of {candidate_list[0]}, {candidate_list[1]}, and {candidate_list[2]}")

