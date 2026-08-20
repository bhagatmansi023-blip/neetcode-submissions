class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 1
        while res in hashset:
            res += 1
        return res