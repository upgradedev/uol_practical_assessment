"""Module of floyd's algorithm test cases."""

import unittest
import threading
from floyds_algorithm import floyd_recursive


class TestFloydAlgorithm(unittest.TestCase):
    """Class representing floyd's algorithm test cases."""

    def test_valid_graph(self):
        """Function to test a valid input graph."""
        input_graph = [
            [0, 5, float('inf'), 10],
            [float('inf'), 0, 3, float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        output_result = floyd_recursive(input_graph, len(input_graph))
        expected_result = [
            [0, 5, 8, 9],
            [float('inf'), 0, 3, 4],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        self.assertEqual(output_result, expected_result)

        # Test case 2: Empty graph
        graph2 = [[]]
        result2 = floyd_recursive(graph2, 0)
        expected_result2 = [[]]
        self.assertEqual(result2, expected_result2)

    def test_invalid_graph(self):
        """Function to test an invalid input graph"""
        graph = {}
        empty_graph_result = floyd_recursive(graph, len(graph))
        self.assertEqual(empty_graph_result, {})

    def test_max_values(self):
        """Function to tast a graph with maximum values."""
        MAX_VALUE = float('inf')
        maxval_graph = [
            [0, MAX_VALUE, MAX_VALUE],
            [MAX_VALUE, 0, MAX_VALUE],
            [MAX_VALUE, MAX_VALUE, 0]
        ]
        expected_result = [
            [0, MAX_VALUE, MAX_VALUE],
            [MAX_VALUE, 0, MAX_VALUE],
            [MAX_VALUE, MAX_VALUE, 0]
        ]

        maxval_graph_result = floyd_recursive(maxval_graph, len(maxval_graph))

        self.assertEqual(
            maxval_graph_result, expected_result,
            "Edge case test for maximum values failed"
            )

    def test_concurrency(self):
        """Function to test the algorithm with multiple threads."""

        # Create a shared variable to store the result of each thread
        shared_result = []

        # Define a function to perform Floyd's algorithm and store the result
        def run_floyd(graph):
            exec_result = floyd_recursive(graph, len(graph))
            shared_result.append(exec_result)

        # Define a test case with known input
        graph = [
            [0, 5, float('inf'), 10],
            [float('inf'), 0, 3, float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]

        # Create multiple threads to run the algorithm concurrently
        threads = []
        for _ in range(5):
            thread = threading.Thread(target=run_floyd, args=(graph,))
            thread.start()
            threads.append(thread)

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Verify that all threads produced the same result
        for result in shared_result[1:]:
            self.assertEqual(
                result, shared_result[0],
                "Concurrency test failed"
                )

    def test_regression(self):
        """Function to test the algorithm with a known input graph."""

        # Define a test case with known input and expected output
        graph = [
            [0, 5, float('inf'), 10],
            [float('inf'), 0, 3, float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        # Store the expected result for the provided graph
        expected_result = [
            [0, 5, 8, 9],
            [float('inf'), 0, 3, 4],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]

        # Perform the Floyd's algorithm
        result = floyd_recursive(graph, len(graph))

        # Compare the result with the expected output
        self.assertEqual(result, expected_result, "Regression test failed")


if __name__ == '__main__':
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFloydAlgorithm)

    # Create a test runner
    runner = unittest.TextTestRunner()

    # Run the test suite
    test_suite_result = runner.run(suite)

    # Print the test results
    print(test_suite_result)
