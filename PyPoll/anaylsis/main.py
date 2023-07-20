# Dependencies
import os
import csv
# Collecting Data
electionData = os.path.join('PyPoll/Resources/election_data.csv')
#Trackers
voteCount = 0
charlesVoteCount = 0
charlesPerc = 0
dianaVoteCount = 0
dianaPerc = 0
raymonVoteCount = 0
raymonPerc = 0
tracker = {}
win = 0 
winner = 0
voteList = []
namesList = []
# Read into csv
with open(electionData) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Header
    header = next(csvreader)

    # Loop
    for row in csvreader:
        # Vote count
        voteCount += 1

        # Tracking votes
        if row[2] == 'Charles Casper Stockham':
            charlesVoteCount +=1
        elif row[2] == 'Diana DeGette':
            dianaVoteCount +=1
        else:
            raymonVoteCount +=1

    # Calculating percentage of votes
    charlesPerc = (charlesVoteCount / voteCount) * 100
    dianaPerc = (dianaVoteCount / voteCount) * 100
    raymonPerc = (raymonVoteCount / voteCount) * 100

    tracker = {'Charles Casper Stockham': charlesVoteCount, 'Diana DeGette': dianaVoteCount, 'Raymon Anthnoy Doane':raymonVoteCount}

    # Calculating Winner 
    for i, t in tracker.items():
        if t > win:
            win = t
            winner = i
print(winner)

# Output Summary
output = (
    f'Election Resluts\n'
    f'-------------------------\n'
    f'Total Votes: {voteCount}\n'
    f'-------------------------\n'
    f'Charles Casper Stockham: {charlesPerc:.3f}% ({charlesVoteCount})\n'
    f'Diana Degette: {dianaPerc:.3f}% ({dianaVoteCount})\n'
    f'Raymon Anthony Doane: {raymonPerc:.3f}% ({raymonVoteCount})\n'
    f'-------------------------\n' 
    f'Winner: {winner}\n'
    f'-------------------------'
)
print(output)

# Creating file and writing into 
file = os.path.join('PyPoll.txt')
file = open('PyPoll.txt', 'w')
file.write(output)
file.close()