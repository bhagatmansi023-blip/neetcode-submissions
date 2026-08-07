class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = set()
        for i in nums:
            if i in num:
                return True
            num.add(i)
        return False
          
obj = Solution()
print(obj.hasDuplicate([1,2,3,3]))        