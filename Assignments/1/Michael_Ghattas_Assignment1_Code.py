##
# Michael Ghattas
# COMP 4581 - Assignment 1
# Feb/10/2025
##



import collections


def loadGraph(edgeFilename):
    """Loads the graph from a given edge list file."""
    graph = collections.defaultdict(set)
    with open(edgeFilename, 'r') as file:
        for line in file:
            u, v = map(int, line.strip().split())
            graph[u].add(v)
            graph[v].add(u)  # Since the graph is undirected
    return graph

class MyQueue:
    """Queue implementation using a list."""
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.empty():
            return self.queue.pop(0)
        raise IndexError("Dequeue from empty queue")
    
    def empty(self):
        return len(self.queue) == 0
    
    def __str__(self):
        return str(self.queue)

def BFS(G, s):
    """Breadth-First Search to compute shortest path distances from s."""
    distances = {node: float('inf') for node in G}
    distances[s] = 0
    q = MyQueue()
    q.enqueue(s)
    
    while not q.empty():
        u = q.dequeue()
        for v in G[u]:
            if distances[v] == float('inf'):
                distances[v] = distances[u] + 1
                q.enqueue(v)
    
    return distances

def distanceDistribution(G):
    """Computes the distribution of shortest path lengths in G."""
    total_distances = collections.Counter()
    nodes = list(G.keys())
    
    for i, node in enumerate(nodes):
        distances = BFS(G, node)
        for dist in distances.values():
            if dist < float('inf') and dist > 0:  # Ignore unreachable nodes and self-distances
                total_distances[dist] += 1
        
        if i % 500 == 0:
            print(f"Processed {i}/{len(nodes)} nodes...")
    
    total_pairs = sum(total_distances.values())
    distribution = {dist: (count / total_pairs) * 100 for dist, count in total_distances.items()}
    return distribution

# Load the graph and compute distance distribution
graph = loadGraph("edges.txt")
distribution = distanceDistribution(graph)

# Print the final distribution with detailed explanation
print("\nDistance Distribution Analysis:\n")
print("The table below represents the percentage of node pairs that are connected by a given shortest path length. ")
print("This helps in understanding how efficiently nodes in the network are connected.")
print("Shorter distances indicate a more tightly connected network, supporting the small-world phenomenon.")
print("\nDistance Distribution (% of total node pairs):\n")
for dist, freq in sorted(distribution.items()):
    print(f"Shortest Path Length {dist}: {freq:.2f}% of all node pairs")


# Analysis of small-world phenomenon:
"""
YES


The small-world phenomenon states that most nodes should be connected by a relatively small number of hops.
If the majority of distances fall within a low range (e.g., within 6 hops), then the network exhibits the small-world property.
Based on the computed distribution, we can determine whether this property holds for our dataset.


The table below represents the percentage of node pairs that are connected by a given shortest path length. 
This helps in understanding how efficiently nodes in the network are connected.
Shorter distances indicate a more tightly connected network, supporting the small-world phenomenon.


Distance Distribution (% of total node pairs):

Shortest Path Length 1: 1.08% of all node pairs
Shortest Path Length 2: 16.65% of all node pairs
Shortest Path Length 3: 24.41% of all node pairs
Shortest Path Length 4: 35.94% of all node pairs
Shortest Path Length 5: 15.73% of all node pairs
Shortest Path Length 6: 4.15% of all node pairs
Shortest Path Length 7: 1.93% of all node pairs
Shortest Path Length 8: 0.10% of all node pairs


The results strongly support the small-world phenomenon:
    - The distribution suggests that most nodes can reach each other in a small number of steps.
    - The well-known six degrees of separation hypothesis is largely satisfied, as 98.96% of all pairs are within 6 hops.
    - The existence of some nodes needing 7 or 8 hops is expected in real-world social networks.
"""



##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##