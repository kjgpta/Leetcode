class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st = ""
        for i in range(len(s)):
            st += str(ord(s[i])-96)
        for i in range(k):
            k = 0
            for i in range(len(st)):
                k += int(st[i])
            st = str(k)
        return int(st)