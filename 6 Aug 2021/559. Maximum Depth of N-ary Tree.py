"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        if not root: return depth
        queue = [root]
        while queue:
                depth +=1
                queue = [child for node in queue if node for child in node.children]
        return depth