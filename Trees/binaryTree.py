#Binary Tree:
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

print(A)


#Recursive Pre Order traversal (DFS), time: o(n), space: o(n)
# def pre_order(node):
#     if not node:
#         return

#     print(node)
#     pre_order(node.left)
#     pre_order(node.right)

# pre_order(A)


#Recursive In Order traversal, 
# def in_order(node):
#     if not node:
#         return

#     in_order(node.left)
#     print(node)
#     in_order(node.right)

# in_order(A)

#Recursive Post Order traversal, 
# def post_order(node):
#     if not node:
#         return

#     in_order(node.left)
#     in_order(node.right)
#     print(node)

# post_order(A)

#Iterative, Pre order, traversal (DFS) time: o(n), space: o(n)
def pre_order_iterative(node):
    stk = [node]
    while stk:
        node = stk.pop()
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)
        print(node)

pre_order_iterative(A)

#Level order traversal (BFS), time: o(n), space: o(n)
from collections import deque
def level_order(node):
    q = deque()
    q = q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

level_order(A)

#Check if a val exist using DFS

def search(node, target):
    if not node:
        return False
    if node == target:
        return True
    
    return search(node.left, target) or search(node.right, target)
search(A, 5)
