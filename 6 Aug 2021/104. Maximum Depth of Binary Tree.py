# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if not root: return depth
        queue = [root]
        next_queue = []
        while queue:
            for root in queue:
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            queue=next_queue
            next_queue=[]
            depth +=1
        return depth