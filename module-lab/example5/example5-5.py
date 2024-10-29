# Definition of a Node in a singly linked list
class Node:
    def __init__(self, data):
       # Data part of the node
        self.data = data
        self.next = None

# Python function to insert a node at the end of the linked
# list
def insert_at_end(head, value):
    # Create a new node with the given value
    new_node = Node(value)

    # If the list is empty, make the new node the head
    if head is None:
        return new_node

    # Traverse the list until the last node is reached
    current = head
    while current.next is not None:
        current = current.next

    # Link the new node to the current last node
    current.next = new_node

    return head

