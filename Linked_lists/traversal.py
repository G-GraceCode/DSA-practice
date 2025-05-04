#traversal, insertion, Deletion, Reversal, Cycle_Detection
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def traverse(head):
    current = head
    while current:
        print(current.data)
        print(current, "current")
        current = current.next
# Example usage
def insert(head, position, data):
    new_node = Node(data)
    if position == 0:
        new_node.next = head
        return new_node
    for _ in range(position - 1):
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

traverse(head)