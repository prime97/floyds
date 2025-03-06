"""
This module has a simple implementation of Floyd's Algorithm
It contains three main functions:
    main -> controls the execution of the script
    print_out_graph -> prints out the graph with nodes and distances
    recursive_floyd_warshall -> computes shortest path

The global variables are:
    NO_PATH = Marker for where there is no path. This is the max value of an integer
    GRAPH = Contains the distances for the graph. Node names are inferred by the position
    of the node, i.e. position  0 0 in the list is node 0
    MAX_LENGTH = The size of the graph
    MIN_LEVEL = The lowest search level for the shortest path calculation
    NO_PATH_MARKER = Holder for no path possible. This is used for the printing function. 
"""
from sys import maxsize

NO_PATH = maxsize
GRAPH = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(GRAPH[0])  #number of vertices (nodes)
MIN_LEVEL = 0
NO_PATH_MARKER = "No Path"


def main():
    recursive_floyd_warshall(MIN_LEVEL, MIN_LEVEL, MIN_LEVEL)
    print_out_graph()


def print_out_graph():
    """This function prints out the graph with the distances
    and a placeholder for no path between nodes
    """
    for start_node in range(0, MAX_LENGTH):
        for end_node in range(0, MAX_LENGTH):
            distance = GRAPH[start_node][end_node]
            if distance == NO_PATH:
                distance = NO_PATH_MARKER  # Replace large number with "No Path"

            message = "Distance from Node %s to Node %s is %s" % \
                      (start_node, end_node, distance)
            print(message)


def recursive_floyd_warshall(outer_loop: int, middle_loop: int, inner_loop: int):
    """outer_loop: acts as an intermediate node,
    middle_loop: acts as a start node,
    inner_loop: acts as an end node
    """
    if outer_loop == MAX_LENGTH:  # Checks if all the intermediate nodes have been checked.
        return

    if middle_loop == MAX_LENGTH:  # Checks if the starting node (middle_loop) reached all the nodes, moves to next outer_loop.
        recursive_floyd_warshall(outer_loop + 1, MIN_LEVEL, MIN_LEVEL)
        return

    if inner_loop == MAX_LENGTH:  # If the end node (inner_loop) reaches all the nodes, moves to the next node
        recursive_floyd_warshall(outer_loop, middle_loop + 1, MIN_LEVEL)
        return

    # Compares the current shortest known path to the new path and updates the matrix with the shortest path
    GRAPH[middle_loop][inner_loop] = min(
        GRAPH[middle_loop][inner_loop],
        GRAPH[middle_loop][outer_loop] + GRAPH[outer_loop][inner_loop]
    )
    recursive_floyd_warshall(outer_loop, middle_loop, inner_loop + 1)


if __name__ == "__main__":
    main()
