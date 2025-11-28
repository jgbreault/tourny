from ..structure.foundation import *

def getWinnerProbabilities(tournament, numSimulations=100000):
    
    teamNames = [team.name for team in tournament.teams]
    winCounts = dict.fromkeys(teamNames, 0)
    
    for i in range(numSimulations):
        
        tourny = Tournament(tournament.teams, tournament.pairingType)
        tourny.runTournament()
        
        winner = tourny.getWinningTeamName()
    
        winCounts[winner] += 1

    return {team: count/numSimulations for team, count in winCounts.items()}