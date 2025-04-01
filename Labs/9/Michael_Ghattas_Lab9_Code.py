##
# Michael Ghattas
# COMP 4581 - Lab 9
# Mar/9/2025
##



import heapq

def prim_mst(graph):
    """
    Implements Prim's Minimum Spanning Tree (MST) algorithm.
    
    Parameters:
        graph (list of list): Adjacency matrix representing the weighted graph.
    
    Returns:
        list: List of edges forming the MST in the format [[vertex1, vertex2], ...].
    """

    num_vertices = len(graph)
    visited = set()
    mst_edges = []
    
    # Min heap to select the next smallest edge
    min_heap = [(0, 0, -1)]  # (weight, current_vertex, previous_vertex)
    
    while len(visited) < num_vertices:
        weight, current_vertex, previous_vertex = heapq.heappop(min_heap)
        
        # Ignore if already visited
        if current_vertex in visited:
            continue
        
        # Add the edge to MST (except the starting node)
        if previous_vertex != -1:
            mst_edges.append([current_vertex, previous_vertex])
        
        # Mark the vertex as visited
        visited.add(current_vertex)
        
        # Explore all adjacent vertices
        for neighbor in range(num_vertices):
            edge_weight = graph[current_vertex][neighbor]
            if neighbor not in visited and edge_weight > 0:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_vertex))
    
    return mst_edges

# Given adjacency matrix (same as in the problem statement)
graph = [
    [0, 7, 0, 0, 0, 10, 15, 0],
    [7, 0, 12, 5, 0, 0, 0, 9],
    [0, 12, 0, 6, 0, 0, 0, 0],
    [0, 5, 6, 0, 14, 8, 0, 0],
    [0, 0, 0, 14, 0, 3, 0, 0],
    [10, 0, 0, 8, 3, 0, 0, 0],
    [15, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0]
]

# Compute MST
mst_result = prim_mst(graph)
print("Minimum Spanning Tree Edges:", mst_result)



##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##