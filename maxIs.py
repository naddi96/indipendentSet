import networkx as nx
import matplotlib.pyplot as plt
import math
from itertools import chain, combinations
import time
from generateGraph import*


#nx.draw(G)
#plt.show()
#plt.savefig("path.png")

def getMin(list):
    min = math.inf
    node=()
    for x in list:
        if(min > x[1]):
            min = x[1]
            node = x
    return node



def greedyIS(Gx):
    G=Gx.copy()
    S = []
    while G.number_of_nodes() != 0:
        x=getMin(G.degree)[0]
        S.append(x)
        G.remove_nodes_from(list(G.neighbors(x)))
        G.remove_node(x)
    return S


def powerset(iterable):
    s = list(iterable) 
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))




def isaIS(G,listOfnode):
    for node in listOfnode:
        for x in G.neighbors(node):
            if x in listOfnode:
                return False
    return True



def maxIS(G):
    max = -math.inf
    S =[]
    for combo in enumerate(powerset(G.nodes), 1):
        if( isaIS(G,combo[1] )):
            if max < len(combo[1]):
                max = len(combo[1])
                S = combo[1]
    return list(S)


def loadGraph():
    file = open("input.txt","r")
    line=file.read().split("\n")
    n = int(line[0].split(" ")[0])
    listOfnode = list(range(0,n))
    G = nx.Graph()
    G.add_nodes_from(listOfnode)
    
    for arch in line[1:]:
        a=arch.split(" ")
        G.add_edge(int(a[0]),int(a[1]))
    return G




generate()
G = loadGraph()

print(len(G.nodes))



print("soluzione approssimata\n")
start_time = time.time()
Sapr = greedyIS(G)
print("--- %s seconds ---\n" % (time.time() - start_time))
print(Sapr)
print("dim:"+str(len(Sapr)))



print()
print()


print("soluzione ottima\n")
start_time = time.time()
Smax = maxIS(G)
print("--- %s seconds ---\n" % (time.time() - start_time))
print(Smax)
print("dim:"+str(len(Smax)))




nx.draw(G,with_labels = True)
plt.show()
#print (greedyIS(G))