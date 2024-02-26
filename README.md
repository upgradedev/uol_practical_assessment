# Floyd's Algorithm Recursive Implementation

This project contains a recursive implementation of Floyd's algorithm in Python, along with performance tests and unit tests.

## Overview

Floyd's algorithm, also known as the Floyd-Warshall algorithm, is used for finding the shortest paths between all pairs of vertices in a weighted graph. This implementation provides a recursive version of the algorithm.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/upgradedev/uol_practical_assessment.git
   ```
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Files

- `floyds_algorithm.py`: Contains the recursive implementation of Floyd's algorithm.
- `tests\performance_test.py`: Performs performance testing of the Floyd's algorithm implementation.
- `tests\unit_test.py`: Contains unit tests for the Floyd's algorithm implementation.

## Usage

To use the Floyd's algorithm recursive implementation, you can import the `floyd_algorithm` module into your Python code:

```python
from floyds_algorithm import floyd_recursive

# Example usage:
# Define your graph
graph = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]
# Perform Floyd's algorithm
shortest_paths = floyd(graph, len(graph))

# Display the shortest paths
for row in shortest_paths:
    print(row)
```

To run the performance test and unit test:

```bash
python -m tests.performance_test
python -m tests.unit_test.py
```

In the performance test module you can set the following options/parameters.
- `-size`: Set the graph size for test (default: 5).
- `--iterations`: Set the number of executions (default: 1).
- `--print-output`: Set this argument if you want to print the solution output of Floyd's recursive algorithm.
- 
```bash
# examples
python -m tests.performance_test --print-output
python -m tests.performance_test --size 10 --iterations 5 --print-output
```


## Dependencies

This project doesn't have any external dependencies beyond the Python standard library.

## Contributing

Contributions to the project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).