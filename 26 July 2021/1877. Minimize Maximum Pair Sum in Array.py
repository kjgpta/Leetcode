class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        ar = []
        for i in range(int(n/2)):
            ar.append(nums[i]+nums[n-1-i])
        return max(ar)