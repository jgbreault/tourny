import random

class Team():

    def __init__(self,
                 name,
                 quality):

        self.name = name
        self.quality = quality

    def probabilityOfWinning(self, opponent):
        return self.quality / (self.quality + opponent.quality)

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

    def hasWinner(self):
        return self.winner != None
    

class Round():

    def __init__(self,
                 matches):

        self.matches = matches

    @property
    def numMatches(self):
        return len(self.matches)

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

    @property
    def numRounds(self):
        return len(self.rounds)

    def addRound(self, teams):
        
        if self.pairingType == 'random':
            teamPairs = self.randomPairing(teams)
        elif self.pairingType == 'similar':
            teamPairs = self.similarPairing(teams)
        elif self.pairingType == 'opposite':
            teamPairs = self.oppositePairing(teams)

        matches = []
        for teamPair in teamPairs:
            matches.append(Match(teamPair))
        
        self.rounds.append(Round(matches))
        
    def randomPairing(self, teams):
        shuffledTeams = random.sample(teams, len(teams))
        return [shuffledTeams[i:i+2] for i in range(0, len(shuffledTeams), 2)]

    def similarPairing(self, teams):
        teamsSorted = sorted(teams, key=lambda team: team.quality)
        return [teamsSorted[i:i+2] for i in range(0, len(teamsSorted), 2)]

    def oppositePairing(self, teams):
        teamsSorted = sorted(teams, key=lambda team: team.quality, reverse=True)
        return [[teamsSorted[i], teamsSorted[len(teamsSorted)-i-1]] for i in range(len(teamsSorted)//2)]
    
    def getWinningTeamName(self):
        return self.rounds[-1].matches[0].winner.name

    def runTournament(self):

        self.addRound(self.teams)
        currentRound = self.rounds[-1]

        while not currentRound.matches[0].hasWinner():

            currentRound.runRound()
            
            isFinals = currentRound.numMatches == 1
        
            if not isFinals:
                
                winningTeams = [match.winner for match in currentRound.matches]
                self.addRound(winningTeams)
                
                currentRound = self.rounds[-1]