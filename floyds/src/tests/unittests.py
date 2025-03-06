"""
This module contains unit tests for both the recursive and iterative versions
of Floyd's algorithm using the `unittest` framework.
"""

import sys
import unittest

# Ensure the correct path to access recursion and iterative modules
sys.path.append('../')

from recursion.recursive_floyd import recursive_floyd_warshall
from iterative.iterative_floyd import iterative_floyd

# Import the global GRAPH variable directly
import recursion.recursive_floyd as recursive_module
import iterative.iterative_floyd as iterative_module


class TestFloydWarshall(unittest.TestCase):
    """
    Unit tests for the Floyd-Warshall Algorithm (Recursive & Iterative).
    """

    def setUp(self):
        """ Reset the global GRAPH variables before each test. """
        self.initial_graph = [
            [0, 7, float('inf'), 8],
            [float('inf'), 0, 5, float('inf')],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0]
        ]

        # Directly modify the GRAPH variables in their respective modules
        recursive_module.GRAPH = [row[:] for row in self.initial_graph]
        iterative_module.GRAPH = [row[:] for row in self.initial_graph]

    def test_recursive_floyd_warshall(self):
        """ Test the recursive Floyd-Warshall algorithm. """
        recursive_floyd_warshall(0, 0, 0)

        expected_result = [
            [0, 7, 12, 8],
            [float('inf'), 0, 5, 7],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0]
        ]

        self.assertEqual(recursive_module.GRAPH, expected_result, "Recursive Floyd-Warshall failed!")

    def test_iterative_floyd_warshall(self):
        """ Test the iterative Floyd-Warshall algorithm. """
        iterative_floyd()

        expected_result = [
            [0, 7, 12, 8],
            [float('inf'), 0, 5, 7],
            [float('inf'), float('inf'), 0, 2],
            [float('inf'), float('inf'), float('inf'), 0]
        ]

        self.assertEqual(iterative_module.GRAPH, expected_result, "Iterative Floyd-Warshall failed!")


if __name__ == "__main__":
    unittest.main()
