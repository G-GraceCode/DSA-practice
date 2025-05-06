#Binary Search Tree (BST)

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)

A = TreeNode(5)
B = TreeNode(1)
C = TreeNode(8)
D = TreeNode(-1)
E = TreeNode(3)
F = TreeNode(7)
G = TreeNode(9)

A.left, A.right = B, C
B.left, B.right= D, E
C.left, C.right = F, G

# print(A)

def in_order(node):
    if not node:
        return

    in_order(node.left)
    print(node)
    in_order(node.right)
in_order(A)

#Let search for something in a tree, using BSTs, Time: o(log n), space: o(log n)
def search_bst(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    if target < node.val :
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)

result = search_bst(A, 10)
print(result)

#note, Binary Search Tree, (BST) search faster than a Binary Tree (DFS)