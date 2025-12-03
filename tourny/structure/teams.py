from .foundation import *

def countTeams(teams):
    return len(teams)

def sortTeamsByQuality(teams):
    teams.sort(key=lambda t: t.quality, reverse=True)

def getBestTeams(teams):

    bestTeams = []
    bestQuality = max([team.quality for team in teams])
    
    for team in teams:
        if team.quality == bestQuality:
            bestTeams.append(team)

    return bestTeams

    

########## Quidditch Teams (Size: 4) ##########

gryffindor = HogwartsHouse('Gryffindor', 100, 'red')
slytherin = HogwartsHouse('Slytherin', 90, 'green')
ravenclaw = HogwartsHouse('Ravenclaw', 20, 'blue')
hufflepuff = HogwartsHouse('Hufflepuff', 10, 'yellow')

quidditch = [
    gryffindor,
    slytherin,
    ravenclaw,
    hufflepuff
]


########## Top Chess Players (Size: 8) ##########

magnusCarlsen = ChessPlayer('Magnus Carlsen', 100, 'Norway')
hikaruNakamura = ChessPlayer('Hikaru Nakamura', 92, 'USA')
dingLiren = ChessPlayer('Ding Liren', 87, 'China')
alirezaFirouzja = ChessPlayer('Alireza Firouzja', 85, 'Iran')
ianNepomniachtchi = ChessPlayer('Ian Nepomniachtchi', 80, 'Russia')
fabianoCaruana = ChessPlayer('Fabiano Caruana', 72, 'USA')
anishGiri = ChessPlayer('Anish Giri', 60, 'Netherlands')
levonAronian = ChessPlayer('Levon Aronian', 44, 'Armenia')

chess = [
    magnusCarlsen,
    hikaruNakamura,
    dingLiren,
    alirezaFirouzja,
    ianNepomniachtchi,
    fabianoCaruana,
    anishGiri,
    levonAronian
]


########## Avengers (Size: 16) ##########

scarletWitch = Superhero('Scarlet Witch', 100, 'Magic')
thor = Superhero('Thor', 98, 'Magic')
hulk = Superhero('Hulk', 95, 'Strength')
captainMarvel = Superhero('Captain Marvel', 94, 'Energy')
doctorStrange = Superhero('Doctor Strange', 92, 'Magic')
vision = Superhero('Vision', 90, 'Tech')
ironMan = Superhero('Iron Man', 40, 'Tech')
spiderMan = Superhero('Spider-Man', 30, 'Agility')
blackPanther = Superhero('Black Panther', 25, 'Agility')
captainAmerica = Superhero('Captain America', 20, 'Agility')
blackWidow = Superhero('Black Widow', 15, 'Agility')
hawkeye = Superhero('Hawkeye', 12, 'Agility')
falcon = Superhero('Falcon', 10, 'Flight')
warMachine = Superhero('War Machine', 8, 'Tech')
antMan = Superhero('Ant-Man', 5, 'Size Manipulation')
starlord = Superhero('Star-Lord', 4, 'Tech')

avengers = [
    scarletWitch,
    thor,
    hulk,
    captainMarvel,
    doctorStrange,
    vision,
    ironMan,
    spiderMan,
    blackPanther,
    captainAmerica,
    blackWidow,
    hawkeye,
    falcon,
    warMachine,
    antMan,
    starlord
]


########## NHL Teams (Size: 32) ##########

torontoMapleLeafs = HockeyTeam('Toronto Maple Leafs', 100, 'Leaf')
edmontonOilers = HockeyTeam('Edmonton Oilers', 99, 'Human')
vancouverCanucks = HockeyTeam('Vancouver Canucks', 98, 'Orca')
montrealCanadiens = HockeyTeam('Montreal Canadiens', 97, 'Human')
calgaryFlames = HockeyTeam('Calgary Flames', 96, 'Dog')
winnipegJets = HockeyTeam('Winnipeg Jets', 95, 'Moose')
ottawaSenators = HockeyTeam('Ottawa Senators', 94, 'Human')
coloradoAvalanche = HockeyTeam('Colorado Avalanche', 60, 'Human')
bostonBruins = HockeyTeam('Boston Bruins', 57, 'Bear')
pittsburghPenguins = HockeyTeam('Pittsburgh Penguins', 56, 'Penguin')
vegasGoldenKnights = HockeyTeam('Vegas Golden Knights', 55, 'Human')
tampaBayLightning = HockeyTeam('Tampa Bay Lightning', 54, 'Bug')
newYorkRangers = HockeyTeam('New York Rangers', 53, 'Human')
carolinaHurricanes = HockeyTeam('Carolina Hurricanes', 52, 'Human')
floridaPanthers = HockeyTeam('Florida Panthers', 51, 'Cat')
newJerseyDevils = HockeyTeam('New Jersey Devils', 50, 'Mythical')
minnesotaWild = HockeyTeam('Minnesota Wild', 49, 'Bear')
newYorkIslanders = HockeyTeam('New York Islanders', 48, 'Dog')
dallasStars = HockeyTeam('Dallas Stars', 47, 'Human')
seattleKraken = HockeyTeam('Seattle Kraken', 46, 'Mythical')
losAngelesKings = HockeyTeam('Los Angeles Kings', 45, 'Lion')
stLouisBlues = HockeyTeam('St. Louis Blues', 44, 'Human')
anaheimDucks = HockeyTeam('Anaheim Ducks', 43, 'Duck')
nashvillePredators = HockeyTeam('Nashville Predators', 42, 'Cat')
utahMammoth = HockeyTeam('Utah Mammoth', 41, 'Mammoth')
detroitRedWings = HockeyTeam('Detroit Red Wings', 40, 'Octopus')
sanJoseSharks = HockeyTeam('San Jose Sharks', 39, 'Shark')
buffaloSabres = HockeyTeam('Buffalo Sabres', 38, 'Sabre-tooth')
philadelphiaFlyers = HockeyTeam('Philadelphia Flyers', 37, 'Human')
columbusBlueJackets = HockeyTeam('Columbus Blue Jackets', 36, 'Insect')
chicagoBlackhawks = HockeyTeam('Chicago Blackhawks', 35, 'Human')
arizonaCoyotes = HockeyTeam('Arizona Coyotes', 34, 'Coyote')

hockey = [
    torontoMapleLeafs,
    edmontonOilers,
    vancouverCanucks,
    montrealCanadiens,
    calgaryFlames,
    winnipegJets,
    ottawaSenators,
    coloradoAvalanche,
    bostonBruins,
    pittsburghPenguins,
    vegasGoldenKnights,
    tampaBayLightning,
    newYorkRangers,
    carolinaHurricanes,
    floridaPanthers,
    newJerseyDevils,
    minnesotaWild,
    newYorkIslanders,
    dallasStars,
    seattleKraken,
    losAngelesKings,
    stLouisBlues,
    anaheimDucks,
    nashvillePredators,
    utahMammoth,
    detroitRedWings,
    sanJoseSharks,
    buffaloSabres,
    philadelphiaFlyers,
    columbusBlueJackets,
    chicagoBlackhawks,
    arizonaCoyotes
]