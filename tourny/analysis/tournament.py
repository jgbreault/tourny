from ..structure.foundation import Tournament

def getWinnerProbabilities(tournament, numSimulations=100000):
    
    teamNames = getTeamNames(tournament)
    winCounts = initializeWinCounts(teamNames)
    
    for i in range(numSimulations):
        
        tournament.runTournament()
        
        winner = tournament.rounds[-1].matches[0].winner.name
    
        winCounts[winner] += 1

    return {team: count/numSimulations for team, count in winCounts.items()}

def getTeamNames(tournament):
    return [team.name for team in tournament.teams]

def initializeWinCounts(teamNames):
    return dict.fromkeys(teamNames, 0)