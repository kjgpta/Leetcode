"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        tra = []
        def func(node):
            if node:
                for child in node.children:
                    func(child)
                tra.append(node.val)
        func(root)
        return tra