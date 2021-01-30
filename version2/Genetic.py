import math
import turtle
import matplotlib.pyplot as plt
import time
from random import randint
import random
from numpy import random as npR
import operator

class Individual:

    def __init__(self, solution):
        self.solution = solution
        self.fit = 1
        self.fitness_ratio = 0
    
    def getSolution(self):
        return(self.solution)
    
    def getFitness(self):
        return(self.fit)
    
    def getFitnessRatio(self):
        return(self.fitness_ratio)

    def draw(self, salution):
        t = turtle.Turtle()
        s = t.getscreen()
        t.hideturtle()
        s.clearscreen()
        t.pencolor('blue')
        t.goto(0,0)
        q = 1
        # for cor in salution:
        #     t.speed(0)
        #     t.penup()
        #     t.goto(cor[0]*q,cor[1]*q)
        #     t.dot()
        # t.goto(0,0)
        t.dot()
        for cor in salution:
            t.speed(0.0001)
            t.pendown()
            t.goto(cor[0]*q, cor[1]*q)
        t.goto(0,0)
    

    def fitness(self):
        solution = self.getSolution()
        tot = 0

        #tot += math.sqrt(solution[0][0] + solution[0][1]**2)
        for i in range(len(solution)-1):
            tot += math.sqrt((solution[i][0] - solution[i+1][0])**2 + (solution[i][1]-solution[i+1][1])**2)
        #tot += math.sqrt(solution[-1][0] + solution[-1][1]**2)

        self.fit = 1/tot**2
        #print(1/self.fit)
    
    def mutate(self):
        solution = self.getSolution()
        n = len(solution)
        x_1 = int(npR.uniform()*n)
        x_2 = int(npR.uniform()*n)

        keep = solution[x_1]
        solution[x_1] = solution[x_2]
        solution[x_2] = keep
        self.solution = solution

    def setFitness2Population(self, total):
        self.fitness_ratio = self.fit/total
    
    def evolve(self):
        #self.fitness()
        self.draw(self.getSolution())
     
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

if __name__ == "__main__":
    
    number_of_points = 35 # points
    population_total = 15
    mutation_rate = 0.3
    solution = [[146, 130], [113, -118], [201, 156], [11, 212], [-4, -230], [300, 26], [157, -29], [-23, 215], [-283, -82], [-81, -173], [203, -155], [-141, -220], [188, 77], [-139, 295], [93, -268], [283, -208], [134, -193], [-74, -153], [-33, -116], [-249, -38], [-261, 46], [-277, -225], [-139, -42], [189, 156], [63, 10], [25, 150], [276, 53], [-95, -19], [164, 85], [82, 105], [61, -122], [-25, 7], [-299, 228], [244, 120], [248, 
44]]
    #generate(number_of_points)
    population = []

    for i in range(population_total):
        scramble = shuffle(solution)
        population.append(Individual(scramble))
    
    for i in range(1000):
        print('GENERATION :', i, round(1/population[0].getFitness()))
        population_fitness = 0
        
        for genome in population:
            genome.fitness()
            population_fitness += genome.getFitness()
            
        for genome in population:
            genome.setFitness2Population(population_fitness)

        sorted_population = sorted(population, key=operator.attrgetter('fitness_ratio'))
        sorted_population.reverse()
        population.clear()
        sorted_population[0].draw(sorted_population[0].getSolution())
        population.append(sorted_population[0])
        population.append(sorted_population[1])

        for _ in range(population_total-2):

            option_1 = pick(sorted_population)
            option_2 = pick(sorted_population)
            new_genome = Individual(crossover2(option_1, option_2))
            if npR.uniform() < mutation_rate:
                #print('MUTATE')
                new_genome.mutate()
            population.append(new_genome)
        
print('Done')