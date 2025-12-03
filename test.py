from tourny.structure.foundation import Tournament
from tourny.visualization import tournament as tournyViz
from tourny.visualization import analysis as analysisViz
from tourny.structure.teams import avengers
from tourny.structure.teams import quidditch

#Using the avengers object tests the teams.py module in the structure sub package
tourn = Tournament(avengers)

#These 2 visualization functions below test both the visualization and analysis subpackages all in one
analysisViz.pieTournament(tourn)
analysisViz.pieTeam(tourn, 'Iron Man')

#The run tournament function essentially tests nearly the entire foundation module of the structure subpackage
tourn.runTournament()
tournyViz.treeTournament(tourn)

#2nd test
tourn2 = Tournament(quidditch)
tourn2.runTournament()
tournyViz.treeTournament(tourn2)
