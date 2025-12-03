import random

class Team():

    def __init__(self,
                 name,
                 quality):

        self.name = name
        self.quality = quality

    def __str__(self):
        return f'name: {self.name}, quality: {self.quality}'

    def probabilityOfWinning(self, opponent):
        return self.quality / (self.quality + opponent.quality)

class HogwartsHouse(Team):

    def __init__(self,
                 name,
                 quality,
                 houseColour):

        super().__init__(name, quality)
        self.houseColour = houseColour

    def __str__(self):
        return super().__str__() + f', houseColour: {self.houseColour}'

class Superhero(Team):

    def __init__(self,
                 name,
                 quality,
                 power):

        super().__init__(name, quality)
        self.power = power

    def __str__(self):
        return super().__str__() + f', power: {self.power}'

class ChessPlayer(Team):

    def __init__(self,
                 name,
                 quality,
                 homeCountry):

        super().__init__(name, quality)
        self.homeCountry = homeCountry

    def __str__(self):
        return super().__str__() + f', homeCountry: {self.homeCountry}'

class HockeyTeam(Team):

    def __init__(self,
                 name,
                 quality,
                 mascot):

        super().__init__(name, quality)
        self.mascot = mascot

    def __str__(self):
        return super().__str__() + f', mascot: {self.mascot}'

class Match():

    def __init__(self,
                 teams):

        self.teams = teams
        self.winner = None

    def runMatch(self):
        team1 = self.teams[0]
        team2 = self.teams[1]

        team1Won = random.random() < team1.probabilityOfWinning(team2)
        
        if team1Won:
            self.winner = team1
        else:
            self.winner = team2
    
class Round():

    def __init__(self,
                 matches):

        self.matches = matches

    def runRound(self):
        for match in self.matches:
            match.runMatch()
            
class Tournament():

    def __init__(self,
                 teams,
                 pairingType = 'random'):

        self.teams = teams
        self.pairingType = pairingType
        self.rounds = []

    def addRound(self, teams):
        
        if self.pairingType == 'random':
            shuffledTeams = random.sample(teams, len(teams))
            teamPairs = [shuffledTeams[i:i+2] for i in range(0, len(shuffledTeams), 2)]
        elif self.pairingType == 'similar':
            teamsSorted = sorted(teams, key=lambda team: team.quality)
            teamPairs = [teamsSorted[i:i+2] for i in range(0, len(teamsSorted), 2)]
        elif self.pairingType == 'opposite':
            teamsSorted = sorted(teams, key=lambda team: team.quality, reverse=True)
            teamPairs = [[teamsSorted[i], teamsSorted[len(teamsSorted)-i-1]] for i in range(len(teamsSorted)//2)]

        matches = []
        for teamPair in teamPairs:
            matches.append(Match(teamPair))
        
        self.rounds.append(Round(matches))
            
    def runTournament(self):

        self.rounds = []

        self.addRound(self.teams)
        currentRound = self.rounds[-1]

        while currentRound.matches[0].winner == None:

            currentRound.runRound()
            
            isFinals = len(currentRound.matches) == 1
        
            if not isFinals:
                
                winningTeams = [match.winner for match in currentRound.matches]
                self.addRound(winningTeams)
                
                currentRound = self.rounds[-1]