# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        def func(curr):
            ls = str(curr.val)
            if curr.left:
                ls += f"({func(curr.left)})"
            elif curr.right:
                ls += "()"
            if curr.right:
                ls += f"({func(curr.right)})"
            return ls
        return func(root)