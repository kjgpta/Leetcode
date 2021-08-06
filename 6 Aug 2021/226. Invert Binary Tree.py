# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.rec(root)
        return root
    def rec(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return 
        self.rec(root.left)
        self.rec(root.right)
        lft=root.left
        rght=root.right
        root.left=rght
        root.right=lft