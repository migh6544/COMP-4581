# Prim’s Minimum Spanning Tree (MST) Implementation

## **Problem Statement**
The goal of this lab is to implement **Prim’s Minimum Spanning Tree (MST) algorithm**, which finds a subset of edges that connects all vertices in a weighted graph with the **minimum possible total edge weight**. 

Prim’s algorithm follows a **greedy strategy**, iteratively selecting the smallest available edge that expands the tree without forming a cycle.

## **Approach**
We adapt **Dijkstra’s shortest path algorithm** from the given lab instructions to construct **Prim’s MST**. The differences are:
- Instead of tracking the shortest paths, we track the **minimum-weight edges** forming an MST.
- We maintain a **priority queue** to always expand the MST with the smallest available edge.
- The MST edges are stored in a list, ensuring no cycles form.

## **Algorithm Explanation**
The algorithm maintains:
1. **A Min-Heap (Priority Queue):** Used to efficiently select the smallest edge to add to the MST.
2. **A Visited Set:** Ensures that we do not re-add vertices.
3. **A List of MST Edges:** Stores the edges forming the MST.

The process works as follows:
1. **Initialize** with an arbitrary start vertex (default: 0) and push `(0, 0, -1)` to the heap.
2. **While MST is incomplete:**
   - Extract the smallest edge from the heap.
   - If the vertex is already in the MST, skip it.
   - Otherwise, mark it as visited and add the edge to the MST.
   - Push all its **unvisited neighbors** into the heap.
3. **Repeat until all vertices are in the MST.**

## **Complexity Analysis**
The implementation uses a **binary heap** (via `heapq`), ensuring efficiency:
- **Heap operations (`push`, `pop`)**: \(O(\log V)\)
- **Edge insertions**: \(O(E \log V)\)
- **Total Complexity**: **\(O(E \log V)\)** (efficient for sparse graphs)

## **Example Execution**
For the given adjacency matrix representation:
```python
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
```
The MST output is:
```
Minimum Spanning Tree Edges: [[1, 0], [3, 1], [2, 3], [5, 3], [4, 5], [7, 1], [6, 0]]
```
This represents the optimal set of edges forming a connected MST with **minimum total weight**.

## **Takeaway**
-   This implementation efficiently constructs an MST using **Prim’s algorithm with a heap-based priority queue**.
-   The approach ensures an optimal selection of edges while maintaining computational efficiency, making it suitable for large graphs.