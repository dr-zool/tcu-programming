from graphviz import Digraph

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# Initialize and allocate memory for tree nodes
firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)

# Connect binary tree nodes
firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode

# Function to visualize the binary tree
def visualize_tree(node):
    dot = Digraph()
    def add_edges(n):
        if n is None:
            return
        dot.node(str(n.data), str(n.data))  # Create a node in the graph
        if n.left:
            dot.edge(str(n.data), str(n.left.data))  # Add edge from parent to left child
            add_edges(n.left)
        if n.right:
            dot.edge(str(n.data), str(n.right.data))  # Add edge from parent to right child
            add_edges(n.right)
    add_edges(node)
    return dot

# Visualize the tree
dot = visualize_tree(firstNode)
dot.render("tree", view=True)  # This will save and open the visualization
