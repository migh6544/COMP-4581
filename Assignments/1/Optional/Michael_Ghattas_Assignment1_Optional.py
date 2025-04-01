##
# Michael Ghattas
# COMP 4581 - Assignment 1
# Feb/10/2025
##


# Answer to question
"""
Yes, the process of tracking distances between vertices can be made scalable by leveraging previously computed shortest paths instead of recomputing everything from scratch when a new vertex is added.

Instead of recalculating the shortest paths for all node pairs from scratch, we can:
    - Compute the shortest paths from the new vertex to existing nodes efficiently.
    - Update the existing distance distribution incrementally without recomputing all pairwise shortest paths.

Efficient Strategy for Updating Distance Distribution:
    - When a new vertex is added, we need to compute its shortest paths to existing vertices.
    - Use Breadth-First Search (BFS) from new to find its distances to other nodes.
    - Update the distance distribution table by incorporating these new shortest paths.
    - If the new vertex creates shortcuts, reduce affected distances in the table.
    - Avoids recomputing all shortest paths by leveraging BFS on just the new node.
"""


# Pseudocode for Efficient Distance Distribution Update
def updateDistanceDistribution(G, distribution, v_new, new_edges):
    """
    Efficiently updates the distance distribution when a new vertex is added.

    :param G: The existing graph (adjacency list representation)
    :param distribution: Current distance distribution (dictionary mapping distances to frequencies)
    :param v_new: The new vertex being added
    :param new_edges: List of tuples (v_new, v_existing) representing new connections
    """

    # Add the new vertex and edges to the graph
    G[v_new] = set()
    for u in new_edges:
        G[v_new].add(u)
        G[u].add(v_new)  # Undirected graph

    # Compute shortest paths from the new vertex using BFS
    new_distances = BFS(G, v_new)

    # Update the existing distribution with new shortest paths
    for v, d in new_distances.items():
        if d > 0:  # Ignore self-distance
            distribution[d] += 1  # Increment the count for distance d

    return distribution



##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##