from ..structure.foundation import Tournament

def getRoundProbablities(tournament, teamName, numSimulations=100000):

    roundCounts = dict.fromkeys(getRoundKeys(tournament), 0)

    for i in range(numSimulations):
        
        tournament.runTournament()
        numRounds = len(tournament.rounds)

        for j in range(numRounds):

            currentRound = tournament.rounds[j]
            roundWinnerNames = getRoundWinnerNames(currentRound)

            if not teamName in roundWinnerNames:

                if j == 0:
                    roundCounts['No Wins'] += 1
                else:
                    roundCounts[f'Round {j}'] += 1

                break

            elif j+1 == numRounds:
                 roundCounts['Undefeated'] += 1
                        
    return {team: count/numSimulations for team, count in roundCounts.items()}

def getRoundKeys(tournament):
    
    tournament.runTournament()
    
    numRounds = len(tournament.rounds)
    roundKeys = ['No Wins'] + [f'Round {i+1}' for i in range(numRounds-1)] + ['Undefeated']

    return ['No Wins'] + [f'Round {i+1}' for i in range(numRounds-1)] + ['Undefeated']

def getRoundWinnerNames(currentRound):
    return [match.winner.name for match in currentRound.matches]

    