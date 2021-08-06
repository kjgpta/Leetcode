# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        value = root.val
        def func(node):
            if not node:
                return 
            if node.val == value and node.left == None and node.right == None:
                return True
            if node.val != value:
                return False
            k = func(node.left)
            if k == False:
                return False
            l = func(node.right)
            if l == False:
                return False
            return True
        return func(root)