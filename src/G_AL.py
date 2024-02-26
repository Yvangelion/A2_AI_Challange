import numpy as np
from prettytable import PrettyTable
import time

#generate random cross of offsprings created through crossover
def crossover(c_1, c_2):
    cut = np.random.randint(len(c_1))
    combine_c_1 = c_1[:cut] + c_2[cut:]
    combine_c_2 = c_2[:cut] + c_1[cut:]
    
    return combine_c_1, combine_c_2

# mutate popluation by introducing random genes
def mutation(c, p_m):
    mutated_c = []
    for val in c:
        if np.random.rand() < p_m:
            mutated_c.append(1 -val)
        else:
            
            mutated_c.append(val)
            
    return mutated_c

# fitness of population 
def fitness(c):
    x = int(''.join(map(str, c)), 2)
    #format output
    x = x**2
    return x

# select parents of generation
def selection(population):
    ans = fitness
    ranked_population = sorted(population, key =ans)
    survival_size = len(ranked_population)//2
    selected_gen = ranked_population[:survival_size]* 2
    
    return selected_gen

# evolution of population mutations 
def evolution(population, p_m):
    num_generation = 0
    
    # evolution of fitness population
    while not check(population):
        population = selection(population)
        
        offspring_list =  []
        
        #mutate 
        for i in range(0, len(population), 2):
            
            c_1, c_2 = population[i], population[i+1]
            offspring =  crossover(c_1,  c_2)
            offspring_list.extend( offspring)
        population = offspring_list
        
        population = [mutation(c, p_m) for c in population]
        
        num_generation += 1

    return num_generation

# check population fitness
def check(population):
    for x in population:
        if fitness(x) == 0:
            return True
    return False

# create population of 6 bits each
def generate_population(n_pop):
    n_genes = 6
    ans = np.random.randint(2, size=(n_pop, n_genes)).tolist()
    return ans

# start data
n_pop_data = [10,100,10,100]
p_mutation_data = [.05,  .05, .2, .2]

# table names col
table = PrettyTable()
table.field_names = ["n_pop", "p_m", "Average # of generations", "Avg Running Time (milliseconds)"]

for n, p in zip(n_pop_data, p_mutation_data):
    # starting values
    n_pop = n 
    p_mutation = p 
    num_tests = 50  
    total_gens = 0
    total_running_time = 0

    start_pop = generate_population(n_pop)
    
    # running each test
    for i in range(num_tests):
        start_time = time.time()
        n_generations = evolution(start_pop, p_mutation)
        end_time = time.time()

        total_gens += n_generations
        total_running_time += (end_time - start_time) * 1000 

    # calc stats after tests
    avg_gens = round((total_gens /num_tests), 3)
    avg_time = round((total_running_time / num_tests), 3)

    table.add_row([n_pop, p_mutation, avg_gens, avg_time])

# show table
print(table)


