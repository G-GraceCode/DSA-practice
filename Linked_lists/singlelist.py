#Single Node

class SingleNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        # def __str__(self):
        #     return str(self.val)
    
#Traversal time: o(n)
def traversal(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next

#you can display them well
def display(head):
    curr = head
    list = []
    while curr:
        list.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(list))

#Search for a node vale

def search(head, value):
    curr = head
    while curr:
        if curr.val == value :
            return print(True)
        curr = curr.next
    return print(False)

head = SingleNode(1)
C = SingleNode(9)
D = SingleNode(3)
G = SingleNode(2)

head.next = C
C.next = D
D.next = G

traversal(head)
display(head)
search(head, 2)