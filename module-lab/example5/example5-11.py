# Deletion for Binary Tree
from collections import deque

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# Function to delete a node from the binary tree
def deleteNode(root, val):
    if root is None:
        return None

    # Use a queue to perform BFS
    queue = deque([root])
    target = None

    # Find the target node
    while queue:
        curr = queue.popleft()

        if curr.data == val:
            target = curr
            break
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    if target is None:
        return root

    # Find the deepest rightmost node and its parent
    last_node = None
    last_parent = None
    queue = deque([(root, None)])

    while queue:
        curr, parent = queue.popleft()
        last_node = curr
        last_parent = parent

        if curr.left:
            queue.append((curr.left, curr))
        if curr.right:
            queue.append((curr.right, curr))

    # Replace target's value with the last node's value
    target.data = last_node.data

    # Remove the last node
    if last_parent:
        if last_parent.left == last_node:
            last_parent.left = None
        else:
            last_parent.right = None
    else:
        return None
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
    root.left.right = Node(6)

    print("Original tree (in-order): ", end="")
    inorder(root)
    print()

    val_to_del = 3
    root = deleteNode(root, val_to_del)

    print(f"Tree after deleting {val_to_del} (in-order): ", end="")
    inorder(root)
    print()
