class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        k = sorted(milestones,reverse = True)
        t = sum(k) - k[0]
        if k[0] <= t+1:
            return sum(k)
        else:
            return 2*t+ 1