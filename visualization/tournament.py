import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
import glob, re
from datetime import datetime
from ..structure.foundation import Tournament
from ..structure.foundation import Team

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

    pass

def addRoundEdges(edges, round_, previousRound) :

    for match in round_.matches :
        edgeCount = 0
        team1 = match.teams[0]
        team2 = match.teams[1]

        for pMatch in previousRound.matches :
            if edgeCount >= 2: 
                break

            if team1 is pMatch.teams[0] :
                edges.append((team1.name+" vs "+team2.name, pMatch.teams[0].name+" vs "+pMatch.teams[1].name, 
                {'label': 'Winner: '+pMatch.winner.name}))
                edgeCount = edgeCount+1

            if edgeCount < 2 and team1 is pMatch.teams[1] :
                edges.append((team1.name+" vs "+team2.name, pMatch.teams[0].name+" vs "+pMatch.teams[1].name, 
                {'label': 'Winner: '+pMatch.winner.name}))
                edgeCount = edgeCount+1

            if edgeCount < 2 and team2 is pMatch.teams[0] :
                edges.append((team1.name+" vs "+team2.name, pMatch.teams[0].name+" vs "+pMatch.teams[1].name, 
                {'label': 'Winner: '+pMatch.winner.name}))
                edgeCount = edgeCount+1

            if edgeCount < 2 and team2 is pMatch.teams[1] :
                edges.append((team1.name+" vs "+team2.name, pMatch.teams[0].name+" vs "+pMatch.teams[1].name, 
                {'label': 'Winner: '+pMatch.winner.name}))
                edgeCount = edgeCount+1

def treeTournament(tourn, fileName = None) :
    G = nx.DiGraph()

    edges = []
    rounds = tourn.rounds 
    i = 1

    while i < len(rounds):
        addRoundEdges(edges, rounds[i], rounds[i-1])
        i=i+1
    G.add_edges_from(edges)

    #pos = nx.spring_layout(G)
    #pos = graphviz_layout(G, prog="dot")
    pos = nx.nx_pydot.graphviz_layout(G, prog="dot")
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', arrows=True)
    #nx.draw(G, pos, with_labels=True)
    plt.title("Tree Diagram with NetworkX and Matplotlib")
    
    if not fileName :
        fileName = getNewFileName("TournamentTree")
    plt.savefig(fileName+".svg")
    plt.show()