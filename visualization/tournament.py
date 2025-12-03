import glob, re
from datetime import datetime
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
from ..structure.foundation import Tournament

def getNewFileName(name):
    dateString = datetime.now().strftime("%Y-%m-%d")
    prefixString = name+"-"+dateString
    
    if(len(glob.glob(prefixString+".svg")) < 1) :
        return prefixString

    possibleFilesList = glob.glob(prefixString+"-?*.svg")
    integerList = []
    for fileName in possibleFilesList :
        if re.fullmatch(rf"{prefixString}-[0-9]+.svg", fileName):
            integerList.append(int(fileName.split("-")[4].split(".")[0]))

    if len(integerList) < 1 :
        return prefixString+"-1"
    
    return prefixString+"-"+str(1+max(integerList))

def appendEdge(edgeList, previousMatch, newMatch) :
    team1 = newMatch.teams[0]
    team2 = newMatch.teams[1]

    pTeam1 = previousMatch.teams[0]
    pTeam2 = previousMatch.teams[1]

    edgeList.append((pTeam1.name+" vs "+pTeam2.name, team1.name+" vs "+team2.name,
                {'label': 'Winner: '+previousMatch.winner.name}))

def addRoundEdges(edges, round_, previousRound) :

    for match in round_.matches :
        edgeCount = 0
        team1 = match.teams[0]
        team2 = match.teams[1]

        for pMatch in previousRound.matches :
            if edgeCount >= 2: 
                break

            if team1 is pMatch.teams[0] :
                appendEdge(edges, pMatch, match)
                edgeCount = edgeCount+1

            if edgeCount < 2 and team1 is pMatch.teams[1] :               
                appendEdge(edges, pMatch, match)
                edgeCount = edgeCount+1

            if edgeCount < 2 and team2 is pMatch.teams[0] :               
                appendEdge(edges, pMatch, match)
                edgeCount = edgeCount+1

            if edgeCount < 2 and team2 is pMatch.teams[1] :  
                appendEdge(edges, pMatch, match)
                edgeCount = edgeCount+1

def treeTournament(tourn, fileName = None) :
    G = nx.DiGraph()

    edges = []
    rounds = tourn.rounds 
    i = 1

    while i < len(rounds):
        addRoundEdges(edges, rounds[i], rounds[i-1])
        i=i+1

    finalRound = rounds[-1]
    finalMatch = finalRound.matches[0]
    winner = finalRound.matches[0].winner.name
    edges.append((finalMatch.teams[0].name+" vs "+finalMatch.teams[1].name, "Winner is '"+winner+"'",
                {'label': 'Winner: '+winner}))

    G.add_edges_from(edges)

    #pos = nx.spring_layout(G)
    pos = nx.nx_pydot.graphviz_layout(G, prog="dot")
    nx.draw(G, pos, node_color='skyblue', node_size=2000, edge_color='gray', arrows=True)
    
    label_objects = nx.draw_networkx_labels(G, pos, font_size= 8)
    for node, text_obj in label_objects.items():
        text_obj.set_rotation(35)

    plt.title("Tournament Outcome:")
    if not fileName :
        fileName = getNewFileName("TournamentTree")
    plt.savefig(fileName+".svg")
    plt.show()