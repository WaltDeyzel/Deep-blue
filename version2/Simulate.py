from Genome import Genome
import operator
import time
from numpy import random as npR
from Breeding import *

class Simulate:

    def __init__(self, number_of_points, population_total, mutation_rate, solution):
        self.number_of_points = number_of_points
        self.population_total = population_total
        self.mutation_rate = mutation_rate
        self.solution = solution
        self.population = []
    
    def run(self):
        for _ in range(self.population_total):
            scramble = shuffle(self.solution)
            self.population.append(Genome(scramble))
    
        for i in range(1000):
            print('GENERATION :', i, round(1/self.population[0].getFitness()))
            population_fitness = 0
            
            for genome in self.population:
                genome.fitness()
                population_fitness += genome.getFitness()
                
            for genome in self.population:
                genome.setFitness2Population(population_fitness)

            sorted_population = sorted(self.population, key=operator.attrgetter('fitness_ratio'))
            sorted_population.reverse()
            self.population.clear()
            sorted_population[0].draw(sorted_population[0].getSolution())
            self.population.append(sorted_population[0])
            self.population.append(sorted_population[1])

            for _ in range(self.population_total-2):

                option_1 = pick(sorted_population)
                option_2 = pick(sorted_population)
                new_genome = Genome(crossover2(option_1, option_2))
                if npR.uniform() < self.mutation_rate:
                    new_genome.mutate()
                self.population.append(new_genome)



if __name__ == "__main__":

    solution = generate(5)
    test_1 = Simulate(len(solution), 3, 0.1, solution)
    test_1.run()