# Searching in Binary Tree (Depth-First Search)

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# Function to search for a value in the binary tree using DFS
def searchDFS(root, value):
    # Base case: If the tree is empty or we've reached a leaf node
    if root is None:
        return False
    # If the node's data is equal to the value we are searching for
    if root.data == value:
        return True
    # Recursively search in the left and right subtrees
    left_res = searchDFS(root.left, value)
    right_res = searchDFS(root.right, value)

    return left_res or right_res

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)

    value = 6
    if searchDFS(root, value):
        print(f"{value} is found in the binary tree")
    else:
        print(f"{value} is not found in the binary tree")
