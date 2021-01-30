from Genome import Genome
import operator
import time
from numpy import random as npR
from Breeding import generate, pick, crossover2, shuffle, crossover
import matplotlib.pyplot as plt
import math

class Simulate:

    def __init__(self, number_of_points, population_total, mutation_rate, solution, generations):
        self.number_of_points = number_of_points
        self.population_total = population_total
        self.mutation_rate = mutation_rate
        self.solution = solution
        self.population = []
        self.generations = generations

        self.results = []
    
    def run(self):
        for _ in range(self.population_total):
            scramble = shuffle(self.solution)
            self.population.append(Genome(scramble))
    
        for _ in range(self.generations):
            best_fitness = 1/math.sqrt(self.population[0].getFitness())
            if best_fitness > 1:
                self.results.append(best_fitness)
            population_fitness = 0
            
            for genome in self.population:
                genome.fitness()
                population_fitness += genome.getFitness()
                
            for genome in self.population:
                genome.setFitness2Population(population_fitness)

            sorted_population = sorted(self.population, key=operator.attrgetter('fitness_ratio'))
            sorted_population.reverse()
            self.population.clear()
            self.population.append(sorted_population[0])
            self.population.append(sorted_population[1])

            for _ in range(self.population_total-2):

                option_1 = pick(sorted_population)
                option_2 = pick(sorted_population)
                new_genome = Genome(crossover(option_1, option_2))
                if npR.uniform() < self.mutation_rate:
                    new_genome.mutate()
                self.population.append(new_genome)
        self.population[0].draw(self.population[0].getSolution())
        return self.results



if __name__ == "__main__":

    simulations = 10000
    # population_size = 30
    path = generate(100)
    # sim_1 = Simulate(len(path), population_size, 0.1, path, simulations)
    # sim_2 = Simulate(len(path), population_size, 0.15, path, simulations)
    # sim_3 = Simulate(len(path), population_size, 0.2, path, simulations)
    # sim_4 = Simulate(len(path), population_size, 0.25, path, simulations)
    # sim_5 = Simulate(len(path), population_size, 0.3, path, simulations)
    # sim_6 = Simulate(len(path), population_size, 0.7, path, simulations)

    # plt.plot(sim_1.run()) #BLUE
    # plt.plot(sim_2.run()) #ORANGE
    # plt.plot(sim_3.run()) #GREEN
    # plt.plot(sim_4.run()) #RED
    # plt.plot(sim_5.run()) #PURPLE
    # plt.plot(sim_6.run()) #BROWN
    # plt.show()
   
    mutation_rate = 0.2
    sim_1 = Simulate(len(path), 5, mutation_rate, path, simulations)
    sim_2 = Simulate(len(path), 10, mutation_rate, path, simulations)
    sim_3 = Simulate(len(path), 20, mutation_rate, path, simulations)
    sim_4 = Simulate(len(path), 30, mutation_rate, path, simulations)
    sim_5 = Simulate(len(path), 40, mutation_rate, path, simulations)
    sim_6 = Simulate(len(path), 70, mutation_rate, path, simulations)

    plt.plot(sim_1.run()) #BLUE
    plt.plot(sim_2.run()) #ORANGE
    plt.plot(sim_3.run()) #GREEN
    plt.plot(sim_4.run()) #RED
    plt.plot(sim_5.run()) #PURPLE
    plt.plot(sim_6.run()) #BROWN
    plt.show()