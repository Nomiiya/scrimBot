import random

# Look into discord.py .random person, might be a better solution.

#OW
def _6rand(voiceSize):
    # Get randon numbers for the teams
    team1 = []
    team2 = []
    num = 0

    # Team 1 Random
    while (len(team1) != 6):
        num = random.randrange(0, voiceSize)
        if num not in team1: 
            team1.append(num)
        else:
            pass
    team1.sort()

    # Team 2 Random
    while(len(team2) != 6):
        num = random.randrange(0, voiceSize)
        if num not in team1 and num not in team2:
           team2.append(num)
        else:
            pass
    
    team2.sort()

    return team1, team2

#League
def _5rand(voiceSize):
    # Get randon numbers for the teams
    team1 = []
    team2 = []
    num = 0

    # Team 1 Random
    while (len(team1) != 5):
        num = random.randrange(0, voiceSize)
        if num not in team1: 
            team1.append(num)
        else:
            pass
    team1.sort()

    # Team 2 Random
    while(len(team2) != 5):
        num = random.randrange(0, voiceSize)
        if num not in team1 and num not in team2:
           team2.append(num)
        else:
            pass
    
    team2.sort()

    return team1, team2

# Testing
def _1rand(voiceSize):
    # Get randon numbers for the teams
    team1 = []
    team2 = []
    num = 0

    # Team 1 Random
    while (len(team1) != 1):
        num = random.randrange(0, voiceSize)
        if num not in team1: 
            team1.append(num)
        else:
            pass
    team1.sort()

    # Team 2 Random
    while(len(team2) != 1):
        num = random.randrange(0, voiceSize)
        if num not in team1 and num not in team2:
           team2.append(num)
        else:
            pass
    
    team2.sort()

    return team1, team2