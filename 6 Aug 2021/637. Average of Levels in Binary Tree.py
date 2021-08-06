# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = [root.val]
        ar = [root]
        def func(curr,ar):
            next_ar = []
            if curr == None:
                return 
            for i in ar:
                if i.left != None:
                    next_ar.append(i.left)
                if i.right != None:
                    next_ar.append(i.right)
                inte = []
                for j in next_ar:
                    inte.append(j.val)
            if len(inte) != 0:
                res.append(sum(inte)/len(inte))
            ar = next_ar
            if len(ar) != 0:
                func(ar[0],ar)
        func(root,ar)
        return res