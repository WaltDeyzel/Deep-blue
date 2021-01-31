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

def pick(sorted_population):
    
    x = npR.uniform()
    tot = 0
    for genome in sorted_population:
        tot += genome.getFitnessRatio()
        if(x<=tot):
            return genome 

    return(sorted_population[-1])