import matplotlib.pyplot as plt

class TSPVisualizer:
    def __init__(self, cities):
        self.cities = cities

    def plot_solution(self, best_route):
        """Plot the best route found by the Genetic Algorithm."""
        plt.figure(figsize=(8, 6))
        ordered_cities = [self.cities[i] for i in best_route] + [self.cities[best_route[0]]]
        x, y = zip(*ordered_cities)
        plt.plot(x, y, 'o-', markersize=8, label='Best Route')
        
        # Label each city with its index
        for i, city in enumerate(self.cities):
            plt.text(city[0], city[1], str(i), fontsize=12, ha='right')
        
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.title("Best Found Route - Traveling Salesman Problem")
        plt.legend()
        plt.grid()
        plt.show()
