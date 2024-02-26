import random


import numpy as np

def generate_population(n_pop):
    return np.random.randint(2, size=(n_pop, 6)).tolist()

n_pop = 2
start_pop = generate_population(n_pop)
print(start_pop)


