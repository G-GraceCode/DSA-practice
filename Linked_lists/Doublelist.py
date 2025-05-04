class DoubleNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

        def __str__(self):
            return str(self.val)

head = tail = DoubleNode(1)

#Display the head node
def display(head):
    curr = head
    ele = []
    while curr:
        ele.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(ele))

#Insert node at the beginning
def insert_at_begin(head, tail, val):
    new_node = DoubleNode(val, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_begin(head, tail, 3)

print("head-tail", head.val, tail.val)

#Insert node at the end
def insert_at_end(head, tail, val):
    new_node = DoubleNode(val, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 3)
print("head-tail", head.val, tail.val)

display(head)
