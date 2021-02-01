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
    return(shuf)

def rouletteSelection(sorted_population):
    
    x = npR.uniform()
    tot = 0
    for genome in sorted_population:
        tot += genome.getFitnessRatio()
        if(x<=tot):
            return genome 

    return(sorted_population[0])

def tournamentSelection(sorted_population):
    x_1 = int(npR.uniform()*len(sorted_population))
    x_2 = int(npR.uniform()*len(sorted_population))

    option_1 = sorted_population[x_1]
    option_2 = sorted_population[x_2]

    if option_1.getFitness() < option_2.getFitness():
        return option_2
    return option_1


