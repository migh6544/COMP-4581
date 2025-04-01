##
# Michael Ghattas
# COMP 4581 - Lab 10
# Mar/14/2025
##



class MyStack:
    """Stack ADT with list implementation"""
    def __init__(self, type):
        self.elemType = type
        self.state = []  # Empty list

    def __str__(self):
        return str(self.state)

    def empty(self):
        return len(self.state) == 0

    def push(self, elem):
        assert isinstance(elem, list)
        self.state.append(elem)

    def pop(self):
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state.pop()

    def top(self):
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.state[-1]


def is_feasible(state, node, color, graph):
    """Check if assigning 'color' to 'node' is feasible given the current state"""
    for neighbor in range(node):
        if graph[node][neighbor] and state[neighbor] == color:
            return False  # Adjacent nodes cannot have the same color
    return True


def graphColoring(graph, colors):
    """Backtracking function to find a valid coloring of the graph"""
    n = len(graph)  # Number of nodes
    initialState = [-1] * n  # -1 represents uncolored nodes

    s = MyStack(list)  # Stack for DFS
    s.push(initialState)  # Push initial state

    while not s.empty():
        currentState = s.pop()  # Get current state
        currentNode = currentState.count(-1)  # Next node to color

        # Check if all nodes are colored (solution found)
        if currentNode == 0:
            print([colors[c] for c in currentState])
            return

        # Try assigning a color to the current node
        for colorIndex in range(len(colors) - 1, -1, -1):  # Reverse order for stack processing
            if is_feasible(currentState, n - currentNode, colorIndex, graph):
                childState = currentState.copy()
                childState[n - currentNode] = colorIndex  # Assign color
                s.push(childState)  # Push new state to stack

# Testing the function with given graph and colors
graph = [[False, True, False, False, False, True], 
         [True, False, True, False, False, True], 
         [False, True, False, True, True, False], 
         [False, False, True, False, True, False], 
         [False, False, True, True, False, True], 
         [True, True, False, False, True, False]]

colors = ['r', 'g', 'b']
graphColoring(graph, colors)



##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##