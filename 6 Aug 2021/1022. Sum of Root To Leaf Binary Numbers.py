# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    s = 0
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def traverse(cur: TreeNode, sofar: str):
            if cur.left is None and cur.right is None:
                val = int(sofar + str(cur.val), 2)
                self.s += val
                return
            if cur.left is not None:
                traverse(cur.left, sofar + str(cur.val))
            if cur.right is not None:
                traverse(cur.right, sofar + str(cur.val))
        traverse(root, "")
        return self.s