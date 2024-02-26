"""Module with floyd's recursive function."""

def floyd_recursive(graph, n, memo=None):
    """
    Apply Floyd's algorithm recursively with memoization to compute shortest paths.

    Args:
    - graph: The adjacency matrix representing the graph.
    - n: The number of vertices in the graph.
    - memo: Memoization dictionary to store computed results.

    Returns:
    - The shortest paths matrix.
    """
    # Initialize memoization dictionary if not provided
    if memo is None:
        memo = {}

    # Base case
    if n == 0:
        return graph

    # Check for invalid inputs
    if len(graph) < n:
        print('graph_length', len(graph))
        print('n_value',n)
        raise ValueError("Invalid graph dimensions")

    # Check for negative edge weights
    for i in range(n):
        for j in range(n):
            if graph[i][j] < 0:
                raise ValueError("Negative edge weight detected")

    # Check if result is already memoized
    if (n, tuple(map(tuple, graph))) in memo:
        return memo[(n, tuple(map(tuple, graph)))]

    # Recursive case
    for i in range(len(graph)):
        for j in range(len(graph)):
            for k in range(len(graph)):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    # Memoize the result
    memo[(n, tuple(map(tuple, graph)))] = graph

    # Recursive call to solve subproblem with n-1 vertices
    return floyd_recursive(graph, n - 1, memo)
