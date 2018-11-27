
import numpy as np
import itertools




def exist(prob):
    return np.random.choice([True, False,], 1,p=[prob,1-prob])

  
def generate():
    prob= 0.1
    numberOfnodes = 50
    archList =[]
    for arch in list(itertools.combinations(list(range(0,numberOfnodes)), 2)):
        if exist(prob):
            archList.append(arch)

    string = str(numberOfnodes)+" "+str(len(archList))+"\n"

    for arch in archList:
        string = string+str(arch[0])+" "+str(arch[1])+"\n"

    file = open("input.txt","w")
    file.write(string[:-1])
    file.close()


generate()