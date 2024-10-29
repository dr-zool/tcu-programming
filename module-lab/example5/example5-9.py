# Insertion Operation for Binary Tree
from collections import deque

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# Function to insert a new node in the binary tree
def insert(root, key):
    if root is None:
        return Node(key)

    # Create a queue for level order traversal
    queue = deque([root])

    while queue:
        temp = queue.popleft()

        # If left child is empty, insert the new node here
        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            queue.append(temp.left)

        # If right child is empty, insert the new node here
        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            queue.append(temp.right)

    return root

# In-order traversal
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    print("Inorder traversal before insertion: ", end="")
    inorder(root)
    print()

    key = 6
    root = insert(root, key)

    print("Inorder traversal after insertion: ", end="")
    inorder(root)
    print()
