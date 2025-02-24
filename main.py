import random
from tsp_ga.genetic_algorithm import TravelingSalesmanGA
from tsp_ga.visualization import TSPVisualizer


def generate_cities(num_cities):
    """Generate random city coordinates."""
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_cities)]

def main():
    # Get user input for number of cities
    num_cities = int(input("Enter the number of cities: "))
    cities = generate_cities(num_cities)
    
    # Solve TSP using Genetic Algorithm
    tsp_solver = TravelingSalesmanGA(cities)
    best_route, best_distance = tsp_solver.run()
    
    # Print results
    print("Best Route:", best_route)
    print("Best Distance:", best_distance)
    
    # Visualize the result
    visualizer = TSPVisualizer(cities)
    visualizer.plot_solution(best_route)

if __name__ == "__main__":
    main()
