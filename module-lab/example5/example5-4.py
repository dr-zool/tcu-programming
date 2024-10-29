# Definition of a Node in a singly linked list
class Node:
    def __init__(self, data):
       # Data part of the node
        self.data = data
        self.next = None

# Python function to insert a new node at the beginning of the
# linked list
def insert_at_beginning(head, value):
    # Create a new node with the given value
    new_node = Node(value)

    # Set the next pointer of the new node to the current
    # head
    new_node.next = head

    # Move the head to point to the new node
    head = new_node

    # Return the new head of the linked list
    return head
