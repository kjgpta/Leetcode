class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        k = list(boxes)
        n = len(k)
        res = []
        for i in range(n):
            c = 0
            for j in range(n):
                if i!=j and k[j] == '1':
                    c += abs(i-j)
            res.append(c)
        return res