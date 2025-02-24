import random
import numpy as np

class TravelingSalesmanGA:
    def __init__(self, cities, population_size=50, generations=500, mutation_rate=0.02):
        self.cities = cities
        self.num_cities = len(cities)
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.population = [self.random_route() for _ in range(population_size)]

    def random_route(self):
        """Generate a random route."""
        route = list(range(self.num_cities))
        random.shuffle(route)
        return route

    def route_distance(self, route):
        """Calculate the total distance of a given route."""
        distance = 0
        for i in range(self.num_cities):
            start, end = route[i], route[(i + 1) % self.num_cities]  # Circular route
            distance += np.linalg.norm(np.array(self.cities[start]) - np.array(self.cities[end]))
        return distance

    def fitness(self, route):
        return 1 / (self.route_distance(route) + 1e-6)  # Avoid division by zero

    def select_parents(self):
        """Select parents based on fitness proportionate selection (roulette wheel)."""
        fitness_scores = [self.fitness(route) for route in self.population]
        total_fitness = sum(fitness_scores)
        probabilities = [f / total_fitness for f in fitness_scores]
        return random.choices(self.population, weights=probabilities, k=2)

    def crossover(self, parent1, parent2):
        """Order Crossover (OX) for TSP."""
        start, end = sorted(random.sample(range(self.num_cities), 2))
        child = [-1] * self.num_cities
        child[start:end] = parent1[start:end]
        remaining = [gene for gene in parent2 if gene not in child]
        index = 0
        for i in range(self.num_cities):
            if child[i] == -1:
                child[i] = remaining[index]
                index += 1
        return child

    def mutate(self, route):
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(self.num_cities), 2)
            route[i], route[j] = route[j], route[i]

    def evolve(self):
        new_population = []
        for _ in range(self.population_size // 2):
            parent1, parent2 = self.select_parents()
            child1, child2 = self.crossover(parent1, parent2), self.crossover(parent2, parent1)
            self.mutate(child1)
            self.mutate(child2)
            new_population.extend([child1, child2])
        self.population = sorted(new_population, key=lambda r: self.route_distance(r))[:self.population_size]

    def run(self):
        for _ in range(self.generations):
            self.evolve()
        best_route = min(self.population, key=self.route_distance)
        return best_route, self.route_distance(best_route)
