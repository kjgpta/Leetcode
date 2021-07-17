# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum_val = 0
        if not root:
            return 0
        elif root.val >=low  and root.val <= high:
            sum_val += root.val
        return sum_val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)