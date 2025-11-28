from ..structure.foundation import Tournament

def getRoundProbablities(tournament, teamName, numSimulations=100000):

    tournament.runTournament()
    
    numRounds = len(tournament.rounds)
    roundKeys = ['No Wins'] + [f'Round {i+1}' for i in range(numRounds-1)] + ['Undefeated']
    roundCounts = dict.fromkeys(roundKeys, 0)

    for i in range(numSimulations):
        
        tourny = Tournament(tournament.teams, tournament.pairingType)
        tourny.runTournament()

        for j in range(numRounds):

            currentRound = tourny.rounds[j]
            roundWinnerNames = [match.winner.name for match in currentRound.matches]

            if not teamName in roundWinnerNames:

                if j == 0:
                    roundCounts['No Wins'] += 1
                else:
                    roundCounts[f'Round {j}'] += 1

                break

            elif j+1 == numRounds:
                 roundCounts['Undefeated'] += 1
                        
    return {team: count/numSimulations for team, count in roundCounts.items()}