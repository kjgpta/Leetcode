from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s = list(s)
        k = Counter(s)
        ar = k.values()
        if min(ar) == max(ar):
            return True
        return False