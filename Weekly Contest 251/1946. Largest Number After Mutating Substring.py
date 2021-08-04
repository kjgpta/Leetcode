class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        n = len(num)
        k = list(num)
        t = 0
        for i in range(n):
            s = int(num[i])
            r = change[s]
            if s < r :
                k[i] = str(r)
                t = 1
            elif s == r:
                k[i] = str(r)
            else:
                if t == 1:
                    break
        return "".join(k)