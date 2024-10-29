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