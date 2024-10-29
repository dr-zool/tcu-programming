# Definition of a Node in a singly linked list
class Node:
    def __init__(self, data):
       # Data part of the node
        self.data = data
        self.next = None
# Function to insert a node at a specified position
def insertPos(head, pos, data):
    if pos < 1:
        print("Invalid position!")
        return head

    # Special case for inserting at the head
    if pos == 1:
        new_node = Node(data)
        new_node.next = head
        return new_node

    # Traverse the list to find the node before
    # the insertion point
    prev = head
    count = 1
    while count < pos - 1 and prev is not None:
        prev = prev.next
        count += 1

    # If position is greater than the number of nodes
    if prev is None:
        print("Invalid position!")
        return head

    # Insert the new node at the specified position
    new_node = Node(data)
    new_node.next = prev.next
    prev.next = new_node

    return head
