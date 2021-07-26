class Solution:
    def arrayPairSum(self, s: List[int]) -> int:
        s = sorted(s)
        su = 0
        i = 0
        while(i<len(s)):
            su += min(s[i],s[i+1])
            i += 2
        return su 