# tourny - Tournament Simulator

A Python package to simulate single-elimination tournaments

## Sub-Package 1 (structure) Module 1 (foundation)

Holds classes for Teams, Matches, Rounds, and Tournaments. Together they can be used to simulate single-elimination tournaments. Sub-classes have been defined for HogwartsHouse, Superhero, ChessPlayer, and HockeyTeam using inheritance to simulate tournaments between different types of teams.

Functions:

1. Team.probabilityOfWinning

    Description
   
2. Match.runMatch

    Description

3. Round.runRound

    Description

4. Tournament.addRound

    Description

5. Tournament.runTournament

    Description

## Sub-Package 1 (structure) Module 2 (teams)

Holds predefined lists of Teams to be used in simulations, and functions related to lists of Teams.

1. countTeams

    Description
   
2. sortTeamsByQuality

    Description

3. getBestTeams

    Description

## Sub-Package 2 (analysis) Module 1 (tournament)

Holds functions related to anaylsing Tournaments as a whole. Also contains helper functions for setting up analysis.

1. getWinnerProbabilities

    Description
   
2. getTeamNames

    Description

3. initializeWinCounts

    Description

## Sub-Package 2 (analysis) Module 2 (team)

Holds functions related to anaylsing a specific Team in a Tournament. Also contains helper functions for setting up analysis.

1. getRoundProbablities

    Description
   
2. getRoundKeys

    Description

3. getRoundWinnerNames

    Description

## Sub-Package 3 (visualization) Module 1 (tournament)

Holds functions related to visualizing a single Tournament outcome. Also contains helper functions for setting up visualizations.

1. treeTournament

    Plots a completed tournament in the form of a tree. It shows the pairing for all rounds and the results for all matches.
   
2. helperFunction1

    Description

3. helperFunction1

    Description

## Sub-Package 3 (visualization) Module 2 (analysis)

Holds functions related to visualizing results from the analysis sub-package. Also contains helper functions for setting up visualizations.

1. pieWinnerProbabilities

    Plots a pie chart showing the probability of each team winning a given tournament. Uses the getWinnerProbabilities function from Sub-Package 2 (analysis) Module 1 (tournament).
   
2. pieRoundProbablities

    Plots a pie chart showing the probability of a given team reaching each round in a given tournament, but no farther. Uses the getRoundProbablities function from Sub-Package 2 (analysis) Module 2 (team).

3. piePlot

    Plots a pie chart where the catagories and values are provided in the form of a dictionary. A helper function to assist with plotting in pieWinnerProbabilities and pieRoundProbablities.
