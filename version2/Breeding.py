from random import randint
import random
from numpy import random as npR

def generate(n): 
    cordinates = []
    m = 300
    for _ in range(n):
        cor = [randint(-m, m), randint(-m, m)]
        cordinates.append(cor)

    return cordinates

def shuffle(cordinates):

    shuf = random.sample(cordinates, len(cordinates))
    #print('shuf',cordinates)
    return(shuf)

def pick(sorted_population):
    
    x = npR.uniform()
    tot = 0
    for genome in sorted_population:
        tot += genome.getFitnessRatio()
        if(x<=tot):
            #print('x', x, 'tot', tot)
            return genome 

    return(sorted_population[-1])

def crossover(option_1, option_2):

    path_1 = option_1.getSolution()
    path_2 = option_2.getSolution()
    child = path_1[:int(len(path_1)/2)]

    for cor in path_2:
        if cor not in child:
            child.append(cor)
    return(child)

def crossover2(option_1, option_2):

    path_1 = option_1.getSolution()
    path_2 = option_2.getSolution()

    half = int(len(path_1)/2)
    x = int(npR.uniform()*half)
    y = int(npR.uniform()*half)+half
    child = path_1[x:y]
    for cor in path_2:
        if cor not in child:
            child.append(cor)
    return(child)