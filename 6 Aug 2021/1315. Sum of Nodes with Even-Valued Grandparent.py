# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.func(root)
        return self.res

    def func(self,root):
        if not root:
            return None

        if root.val % 2 == 0:
            if root.left:
                if root.left.left:
                    self.res += root.left.left.val
                if root.left.right:
                    self.res += root.left.right.val

            if root.right:
                if root.right.left:
                    self.res += root.right.left.val
                if root.right.right:
                    self.res += root.right.right.val

        self.func(root.left)
        self.func(root.right)