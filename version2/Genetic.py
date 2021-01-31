import operator
import time
from Genome import Genome
from numpy import random as npR
from Breeding import pick, generate, shuffle
from Crossover import crossover3

if __name__ == "__main__":
    
    number_of_points = 35 # points
    population_total = 15
    mutation_rate = 0.25
    solution = generate(number_of_points)
    population = []

    for i in range(population_total):
        scramble = shuffle(solution)
        population.append(Genome(scramble))
    
    for i in range(500):
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
            option_3 = pick(sorted_population)
            new_genome = Genome(crossover3(option_1, option_2, option_3))
            #new_genome = Genome(crossover2(option_1, option_2))
            if npR.uniform() < mutation_rate:
                new_genome.mutate()
            population.append(new_genome)
        
print('Done')