"""Module providing a function printing python version."""
import random

INF = float('inf')


# Function to generate a random graph
def generate_random_graph(size):
    """Function printing python version."""
    graph = []
    for _ in range(size):
        row = [random.randint(1, 100)
               if random.random() < 0.5
               else INF for _ in range(size)]
        graph.append(row)
    return graph


# A utility function to print the solution
def print_solution(dist, vertices):
    """Function printing python version."""
    print("Following matrix shows the shortest distances\
 between every pair of vertices")
    for i in range(vertices):
        for j in range(vertices):
            if(dist[i][j] == INF):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == vertices-1:
                print()
