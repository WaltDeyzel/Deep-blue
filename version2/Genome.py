import turtle
from numpy import random as npR
import math


class Genome:

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
        t.dot()
        for cor in salution:
            t.speed(0.0001)
            t.pendown()
            t.goto(cor[0]*q, cor[1]*q)
        t.goto(0,0)
    

    def fitness(self):
        solution = self.getSolution()
        tot = 0

        tot += math.sqrt(solution[0][0]**2 + solution[0][1]**2)
        for i in range(len(solution)-1):
            tot += math.sqrt((solution[i][0] - solution[i+1][0])**2 + (solution[i][1]-solution[i+1][1])**2)
        tot += math.sqrt(solution[-1][0]**2 + solution[-1][1]**2)

        self.fit = 1/tot**2
    
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