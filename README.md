# tourny - Tournament Simulator

A Python package to simulate single-elimination tournaments.

## Sub-Package 1 (structure) Module 1 (foundation)

Holds classes for Teams, Matches, Rounds, and Tournaments. Together they can be used to simulate single-elimination tournaments. Sub-classes have been defined for HogwartsHouse, Superhero, ChessPlayer, and HockeyTeam using inheritance to simulate tournaments between different types of teams.

Functions:

1. Tournament.__init(self, teams, pairingType)__  
  
    ATTENTION! The "teams" parameter of this constructor must be a list of team objects of LENGTH 2^x (a power of 2), where x is a positive integer. Otherwise the package cannot be used properly.

2. Team.probabilityOfWinning(opponent)  
  
    Determines and returns the probability of the team winning a match against the 'opponent'.  
  
    **return value** - the probability value between 0 and 1.  
    **parameter - opponent** - the opponent variable of object type "Team".
   
3. Match.runMatch()  
  
    Simulates the match between the 2 associated team objects of this Match instance. Stores the winner team object in the winner attribute of the Match instance.  
  
    **return value** - None

4. Round.runRound()  
  
    Runs all the matches of this Round instance (in the matches attribute).  
  
    **return value** - None

5. Tournament.addRound(teams)  
  
    Adds the next round of matches (Round object) in the tournament to the rounds attribute (list of round objects) of the current Tournament instance. The order for the round of matches is determined from the Tournaments pairing attribute.  
  
    **return value** - None  
    **parameter - teams** - the list of Team objects that are up for the next round.

6. Tournament.runTournament()  
  
    Runs the entire tournament, determining the teams for the first round from the Tournament instance teams attribute and the addRound method.  
  
    **return value** - None

## Sub-Package 1 (structure) Module 2 (teams)

Holds predefined lists of Teams to be used in simulations, and functions related to lists of Teams.

Functions:

1. countTeams(teams)  
  
    Counts the number of teams provided and returns the number of teams.  
    **return value** - number of teams  
    **parameter - teams** - list of teams to count from
   
2. sortTeamsByQuality(teams)  
  
    Sorts the list of teams by their quality attribute, in descending order.   
    **return value** - None
    **parameter - teams** - The list of team objects to sort.

3. getBestTeams(teams)  
  
    Gets the best teams from the given teams list.  
    **return value** - List of teams with the highest quality attribute.  
    **parameter - teams** - List of team objects from which to determine the best teams.

## Sub-Package 2 (analysis) Module 1 (tournament)

Holds functions related to anaylsing Tournaments as a whole. Also contains helper functions for setting up analysis.

Functions:

1. getWinnerProbabilities(tournament, numsimulations = 100000)  
  
    Determines the probability of each team winning the tournament from simulations of the tournament.  
    **return value** - Dictionary with team names as keys and probability of winning as values.  
    **parameter - tournament** - The tournament to determine the winning probabilities.  
    **parameter - numsimulations** - The integer number of simulations used to estimate the probabilities.
   
2. getTeamNames(tournament)  
  
    Gets the names of all teams in a given tournament.
    **return value** - list of team names in the tournament  
    **parameter - tournament** - The tournament instance to get the team names from.

3. initializeWinCounts(teamNames)  
  
    Builds a dictionary to initialize a count of 0 wins for each team name.  
    **return value** - the dictionary with team names as keys and 0 (integer) wins as values.  
    **parameter - teamNames** - The list of team names used to build the dictionary.

## Sub-Package 2 (analysis) Module 2 (team)

Holds functions related to anaylsing a specific Team in a Tournament. Also contains helper functions for setting up analysis.

Functions:

1. getRoundProbablities(tournament, teamName, numsimulations = 100000)  
  
    Determines the probability of a given team making it to each round in a given tournament.  
    **return value** - dictionary with round levels as keys and probabilities as values  
    **parameter - tournament** - The tournament instance to find these probabilities from.  
    **parameter - teamName** - The string name of the team to get the round probabilities on.
    **parameter numSimulations** - THe number of simulations to run in determining these probabilities.
   
2. getRoundKeys(tournament)  
  
    Gets the string representation (keys) for the different rounds in a given tournament.  
    **return value** - List of the round keys (strings)  
    **parameter- tournament** - The tournament object instance to get the round keys from.  

3. getRoundWinnerNames(currentRound)  
  
    Gets the name of the winning teams of each match in the given round.  
    **return value** - list of the round winner names (strings)  
    **parameter - currentRound** - The round object instance to get the winners from.

## Sub-Package 3 (visualization) Module 1 (tournament)

Holds functions related to visualizing a single Tournament outcome. Also contains helper functions for setting up visualizations.

Functions:

1. treeTournament(tourn, fileName = None)

    Plots a completed tournament in the form of a tree diagram. It shows the pairing for all rounds and the results for all matches, including the final winner. The diagram is both displayed and also saved as an SVG file in the current directory.  
    **return value** - None  
    **parameter - tourn** - The tournament object instance that you want to be displayed in the diagram.  
    **parameter - fileName** - The string Name of the file name you wish to save the diagram as in your current directory, if None then it is saved as "treeTournament-currentDate-#.svg" (see getNewFileName method below)
   
2. getNewFileName(name)  
  
    Determines an available integer appended value for the given name and current date and returns the first available fileName in the current directory.  
    **return value** - the string of the first current available file name in the current directory of form "name-currentDate-#.svg".  
    **name** - The string name preceding the desired filename.

3. appendEdge(edgeList, previousMatch, newMatch)  
  
    Appends an edge representation between the previous and current match to the in tree diagrams edge list.  
    **return value** - None  
    **parameter - edgeList** - The list of edges (networkx edge tuples) for the tree diagram representation of a tournament.  
    **parameter - previousMatch** - The Match object instance of the previous match in the previous round of the tournament.  
    **parameter - newMatch** - The Match object instance of the current match in the current round of the tournament.  
      
4. addRoundEdges(edges, round_, previousRound)  
  
    Adds all networkx edge tuples of the tree diagram between associated matches in the current and previous rounds to the edges edge tuple list.  
    **return value** - None  
    **parameter - edges** - The list of edges (networkx edge tuples) for the tree diagram representation of a tournament.  
    **parameter - round_** - The round object instance of the current round in the tournament.  
    **parameter - previousRound** - The round object instance of the pprevious round in the tournament. 

## Sub-Package 3 (visualization) Module 2 (analysis)

Holds functions related to visualizing results from the analysis sub-package. Also contains helper functions for setting up visualizations.

Functions:

1. pieTournament(tournament, fileName = None, numSimulations=100000)  
  
    Plots a pie chart showing the probability of each team winning a given tournament. Uses the getWinnerProbabilities method from Sub-Package 2 (analysis) Module 1 (tournament) and the plotPieTournament method in this module. The pie chart is saved as an SVG file in the current directory.  
  
    **return value** - None  
    **parameter - tournament** - The given tournament object instance.  
    **parameter - fileName** - the String Name of the file you wish to save the pie plot as in your current directory, if None then it is saved as "pieTournament-currentDate-#.svg" (see getNewFileName in subpackage 3 mod 1 for more info)  
    **parameter - numSimulations** - The integer number of simulations to use when determining the probabilities.
   
2. pieTeam(tournament, teamName, fileName = None, numSimulations=100000)

    Plots a pie chart showing the probability of a given team reaching each round in a given tournament, but no farther. Uses the getRoundProbablities function from Sub-Package 2 (analysis) Module 2 (team) and the plotPieTeam method in this module. The pie chart is saved as an SVG file in the current directory.  
  
    **return value** - None  
    **parameter - tournament** - The given tournament object instance. 
    **parameter - teamName** - The string name of the team of which you want to generate this pie plot on. 
    **parameter - fileName** - the String Name of the file you wish to save the pie plot as in your current directory, if None then it is saved as "pieTeam-currentDate-#.svg" (see getNewFileName in subpackage 3 mod 1 for more info)  
    **parameter - numSimulations** - The integer number of simulations to use when determining the probabilities.

3. plotPieTeam(roundProbabilities, teamName, pairingType = None, fileName = None)

    Plots a pie chart where the catagories and values are provided in the form of a dictionary. A helper function to assist with plotting in pieTeam. The pie plot is saved as an SVG in the current directory.  
  
    **return value** - None 
    **parameter - roundProbabilities** - dictionary of 'round number : probability' key value pairs.
    **parameter - teamName** - string of the team name.
    **parameter - pairingType** - string of the pairing type of the tournament.
    **parameter - fileName** - the String Name of the file you wish to save the pie plot as in your current directory, if None then it is saved as "pieTeam-currentDate-#.svg" (see getNewFileName in subpackage 3 mod 1 for more info)  

4. plotPieTournament(winnerProbabilities, pairingType = None, fileName = None)  
  
    Plots a pie chart where the catagories and values are provided in the form of a dictionary. A helper function to assist with plotting in pieTournament method. The pie plot is saved as an SVG in the current directory.  
  
    **return value** - None  
    **parameter - winnerProbabilities** - dictionary of 'team name : probability' key value pairs.   
    **parameter - pairingType** - string of the pairing type of the tournament.  
    **parameter - fileName** - the String Name of the file you wish to save the pie plot as in your current directory, if None then it is saved as "pieTournament-currentDate-#.svg" (see getNewFileName in subpackage 3 mod 1 for more info) 
     

