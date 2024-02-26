"""Performance Test Module."""

import cProfile
import argparse
from helpers.utils import generate_random_graph
from helpers.utils import print_solution
from floyds_algorithm import floyd_recursive


def main():
    """
    Main function for the performance test of Floyd's algorithm.
    """
    parser = argparse.ArgumentParser(
        description="Performance test for Floyd's algorithm."
        )
    parser.add_argument("--size", type=int, default=5,
                        help="Graph size (default: 5)")
    parser.add_argument("--iterations", type=int, default=1,
                        help="Number of executions (default: 1)")
    parser.add_argument("--print-output", action="store_true",
                        help="Print the solution output of Floyd's algorithm")
    args = parser.parse_args()

    graph_sizes = [args.size]
    iterations = args.iterations

    for size in graph_sizes:
        random_graph = generate_random_graph(size)
        print(f"Generated graph with size: {size}x{size}")

        # Profile the function using cProfile
        profiler = cProfile.Profile()
        profiler.enable()
        for _ in range(iterations):
            floyd_result = floyd_recursive(random_graph, len(random_graph))

            # We need only one print output per graph result
            if args.print_output and iterations == 1:
                print_solution(floyd_result, size)

        profiler.disable()

        # Print the profiling results
        print(f"Profiling results for {iterations} iterations:")
        profiler.print_stats()
        print()


if __name__ == "__main__":
    main()
