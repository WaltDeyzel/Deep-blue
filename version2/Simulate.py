from Genome import Genome
import operator
import time
from numpy import random as npR
from Crossover import crossover, crossover2, crossover3
from Breeding import pick, shuffle, generate
import matplotlib.pyplot as plt
import math

class Simulate:

    def __init__(self, number_of_points, population_total, crossover_rate, mutation_rate, solution, generations, crossover):
        self.number_of_points = number_of_points
        self.population_total = population_total
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.solution = solution
        self.population = []
        self.generations = generations

        self.crossover = crossover
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

            while len(self.population) != self.population_total:

                new_genome = pick(sorted_population)

                if npR.uniform() < self.crossover_rate:
                    option_1 = new_genome
                    option_2 = pick(sorted_population)
                    new_genome = Genome(self.crossover(option_1, option_2))

                if npR.uniform() < self.mutation_rate:
                    new_genome.mutate()
                self.population.append(new_genome)

        self.population[0].draw(self.population[0].getSolution())
        return self.results



if __name__ == "__main__":

    simulations = 1000
    crossover_rate = 1
    mutation_rate = 0.25
    population_size = 100
    path_len = 50

    # path = generate(path_len)
    path = [[-273, -1], [215, -65], [55, 142], [-192, -135], [-38, 133], [74, 120], [275, 299], [207, 188], [-153, 37], [82, 208], [1, 182], [-2, 99], [-190, 8], [-281, -128], [129, 36], [163, -129], [262, 242], [-299, 21], [153, 4], [210, 209], [109, -246], [179, -5], [-173, 28], [-156, -180], [268, -97], [238, 25], [-12, -174], [43, 275], [-12, -181], [-195, -217], [297, -54], [-258, 117], [275, -214], [45, 249], [-233, 154], [139, 171], [-194, -4], [295, -271], [101, 37], [-102, -163], [37, 229], [151, -297], [-148, -172], [263, -243], [-232, 230], [-253, 4], [35, 212], [267, -17], [-229, -38], [-11, 59]]
    
    sim_1 = Simulate(path_len, population_size, crossover_rate, mutation_rate, path, simulations, crossover)
    # sim_2 = Simulate(path_len, 30, crossover_rate, mutation_rate, path, simulations, crossover)
    # sim_3 = Simulate(path_len, 30, crossover_rate, mutation_rate, path, simulations, crossover)
    # sim_4 = Simulate(path_len, 30, crossover_rate, mutation_rate, path, simulations, crossover)
    # sim_5 = Simulate(path_len, 30, crossover_rate, mutation_rate, path, simulations, crossover)
    # sim_6 = Simulate(path_len, 30, crossover_rate, mutation_rate, path, simulations, crossover)

    plt.plot(sim_1.run()) #BLUE
    # plt.plot(sim_2.run()) #ORANGE
    # plt.plot(sim_3.run()) #GREEN
    # plt.plot(sim_4.run()) #RED
    # plt.plot(sim_5.run()) #PURPLE
    # plt.plot(sim_6.run()) #BROWN
    plt.show()