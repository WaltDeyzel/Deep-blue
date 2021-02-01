from Genome import Genome
import operator
from numpy import random as npR
from Crossover import crossover, crossover2, crossover3
from Breeding import shuffle, generate, rouletteSelection, tournamentSelection
import matplotlib.pyplot as plt
import math

class Simulate:

    def __init__(self, number_of_points, population_total, crossover_rate, mutation_rate, solution, generations, selection, crossover):
        self.number_of_points = number_of_points
        self.population_total = population_total
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.solution = solution
        self.population = []
        self.generations = generations

        self.crossover = crossover
        self.selection = selection
        self.results = []
    
    def run(self):
        # CREATE POPULATION WITH GIVEN PATH
        for _ in range(self.population_total):
            scramble = shuffle(self.solution)
            self.population.append(Genome(scramble))
        # KEEP TRACK OF THE BEST GENOME IN GIVEN POPULATION. FIRST ITTERATION IS RANDOM.    
        best_genome = self.population[0]
        # RUN AMOUNT OF SIMULATIONS/GENERATIONS SPESIFIED
        for _ in range(self.generations):
            # KEEP TRACK OF THE SUM OF ALL THE POPULATION FITNESS
            population_fitness = 0
            for genome in self.population:
                genome.fitness()
                population_fitness += genome.getFitness()
            # NORMALISE THE FITNESS OF EACH GENOME IN THE POPULATION --- ONLY USED FOR ROULETTE SELECTION
            for genome in self.population:
                genome.setFitness2Population(population_fitness)
            # KEEP A COPY OF THE POPULATION
            sorted_population = self.population.copy()
            # KEEP TRACK OF THE FITTEST GENOME IN THE POPULATION
            best_genome = max(self.population, key=operator.attrgetter('fit'))
            best_fitness = 1/math.sqrt(best_genome.getFitness())
            # ADD THE BEST FITNESS SCORE TO A LIST  
            if best_fitness > 1:
                self.results.append(best_fitness)
            # CLEAR POPULATION TO FILL WITH A NEW GENERATION OF GENOMES
            self.population.clear()
            # COPY OVER THE BEST SOLUTION FROM THE PREVIOUS GENERATION --  THE COPY
            self.population.append(best_genome)
            self.population.append(best_genome)
            # FILL THE REST OF EMPTY POPULATION USING THE SELECTION ALG OF CHOICE.
            while len(self.population) != self.population_total:
                
                new_genome = self.selection(sorted_population)
                # CROSSOVER RATE
                if npR.uniform() < self.crossover_rate:
                    option_1 = new_genome
                    option_2 = self.selection(sorted_population)
                    if self.crossover == crossover3:
                        option_3 = self.selection(sorted_population)
                        new_genome = Genome(self.crossover(option_1, option_2, option_3))
                    else:
                        new_genome = Genome(self.crossover(option_1, option_2))
                # MUTATION RATE
                if npR.uniform() < self.mutation_rate:
                    new_genome.mutate()
                # ADD NEWEST MEMBER TO POPULATION
                self.population.append(new_genome)

        best_genome.draw(best_genome.getSolution())
        print('Fitness : ', best_fitness)
        return self.results



if __name__ == "__main__":

    simulations = 10000
    crossover_rate = 0.7
    mutation_rate = 0.25
    population_size = 30
    path_len = 50

    # path = generate(path_len)
    path = [[-273, -1], [215, -65], [55, 142], [-192, -135], [-38, 133], [74, 120], [275, 299], [207, 188], [-153, 37], [82, 208], [1, 182], [-2, 99], [-190, 8], [-281, -128], [129, 36], [163, -129], [262, 242], [-299, 21], [153, 4], [210, 209], [109, -246], [179, -5], [-173, 28], [-156, -180], [268, -97], [238, 25], [-12, -174], [43, 275], [-12, -181], [-195, -217], [297, -54], [-258, 117], [275, -214], [45, 249], [-233, 154], [139, 171], [-194, -4], [295, -271], [101, 37], [-102, -163], [37, 229], [151, -297], [-148, -172], [263, -243], [-232, 230], [-253, 4], [35, 212], [267, -17], [-229, -38], [-11, 59]]

    sim_1 = Simulate(path_len, population_size, crossover_rate, mutation_rate, path, simulations, tournamentSelection, crossover2)  #BLUE
    # sim_2 = Simulate(path_len, population_size, crossover_rate, mutation_rate, path, simulations, rouletteSelection, crossover3)  #ORANGE
    # sim_3 = Simulate(path_len, population_size, crossover_rate, mutation_rate, path, simulations, rouletteSelection, crossover3) #GREEN
    # sim_4 = Simulate(path_len, population_size, crossover_rate, mutation_rate*0, path, simulations, rouletteSelection, crossover3) #RED
    # sim_5 = Simulate(path_len, population_size, crossover_rate, mutation_rate*0, path, simulations, rouletteSelection, crossover3) #PURPLE
    # sim_6 = Simulate(path_len, population_size, crossover_rate, mutation_rate*0, path, simulations, rouletteSelection, crossover3) #BROWN

    plt.plot(sim_1.run()) #BLUE
    # plt.plot(sim_2.run()) #ORANGE
    # plt.plot(sim_3.run()) #GREEN
    # plt.plot(sim_4.run()) #RED
    # plt.plot(sim_5.run()) #PURPLE
    # plt.plot(sim_6.run()) #BROWN
    plt.show()