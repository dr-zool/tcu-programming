# Using binary tree from csv file
import csv

# Define the TreeNode class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to build the binary tree from CSV data
def build_tree_from_csv(csv_filename):
    # Dictionary to hold references to each node
    nodes = {}

    # Read CSV and create nodes
    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Create nodes and store them in a dictionary
        for row in reader:
            value = int(row['value'])
            if value not in nodes:
                nodes[value] = TreeNode(value)
            node = nodes[value]

            # Handle left child
            if row['left']:
                left_value = int(row['left'])
                if left_value not in nodes:
                    nodes[left_value] = TreeNode(left_value)
                node.left = nodes[left_value]

            # Handle right child
            if row['right']:
                right_value = int(row['right'])
                if right_value not in nodes:
                    nodes[right_value] = TreeNode(right_value)
                node.right = nodes[right_value]

    # Return the root node (assuming the first row has the root)
    root_value = int(list(nodes.keys())[0])
    return nodes[root_value]

# Function to print the binary tree in preorder traversal
def preorder_traversal(node):
    if node:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# Usage example
csv_filename = 'C:/Users/kokus/PycharmProjects/tcu-programming/module-lab/example5/binary_tree.csv'

root = build_tree_from_csv(csv_filename)
print("Preorder traversal of the constructed binary tree:")
preorder_traversal(root)
