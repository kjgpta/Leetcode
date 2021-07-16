class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [100000]*26
        last = [0]*26
        for i in range(0, len(s)):
            first[ord(s[i])-97] = min(first[ord(s[i])-97], i)
            last[ord(s[i])-97] = i
        count = 0
        for i in range(0, 26):
            if(first[i] != 100000):
                count += len(set(s[first[i]+1:last[i]]))
        return count