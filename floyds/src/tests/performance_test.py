"""
This module contains a simple performance test which
compares the recursive version of Floyds algorithm with the
imperative version
"""

import sys
import timeit

sys.path.append('../')
from recursion.recursive_floyd import recursive_floyd_warshall
from iterative.iterative_floyd import iterative_floyd


def performance_test(function_handle):
    start_time = timeit.default_timer()
    function_handle()
    end_time = timeit.default_timer()

    elapsed_time = end_time - start_time    # Compute execution time
    print(f"Execution Time: {elapsed_time:.6f} seconds")

print('')

# Run and compare the recursive and iterative implementations
print("Recursion Test Time")
performance_test(lambda: recursive_floyd_warshall(0, 0, 0))

print('')

print("Iterative Test Time")
performance_test(iterative_floyd)
