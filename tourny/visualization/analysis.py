import pygal 
from ..analysis import tournament as tourny
from ..analysis import team as tournyTeam
from ..structure.foundation import Tournament
from ..visualization.tournament import getNewFileName

def plotPieTournament(winnerProbabilities, pairingType = None, fileName = None):
    pieChart = pygal.Pie(width=1200, legend_at_bottom=True)
    pieChart.title = "Percent chance of each team winning the Tournament"

    if pairingType :
        pieChart.title="Percent chance of each team winning the "+pairingType+" paired Tournament"

    for key, value in winnerProbabilities.items(): 
        pieChart.add(key+" - "+str(value*100)+"%", value*100)

    if not fileName :
        fileName = getNewFileName("pieTournament")

    pieChart.render_to_file(fileName+".svg")

def pieTournament(tournament, fileName = None, numSimulations=100000):
    winnerProbabilities = tourny.getWinnerProbabilities(tournament, numSimulations)
    plotPieTournament(winnerProbabilities, tournament.pairingType, fileName)

def plotPieTeam(roundProbabilities, teamName, pairingType = None, fileName = None):
    pieChart = pygal.Pie(width=1200,legend_at_bottom=True)
    pieChart.title = "Percent chance of team '"+teamName+"' making it to each round of the Tournament"

    if pairingType :
        pieChart.title="Percent chance of team '"+teamName+"' making it to each round of the "+pairingType+" paired Tournament"

    for key, value in roundProbabilities.items(): 
        pieChart.add(key+" - "+str(value*100)+"%", value*100)

    if not fileName :
        fileName = getNewFileName("pieTeam")

    pieChart.render_to_file(fileName+".svg")

def pieTeam(tournament, teamName, fileName = None, numSimulations=100000):
    roundProbabilities = tournyTeam.getRoundProbablities(tournament, teamName, numSimulations)
    plotPieTeam(roundProbabilities, teamName, tournament.pairingType, fileName)
