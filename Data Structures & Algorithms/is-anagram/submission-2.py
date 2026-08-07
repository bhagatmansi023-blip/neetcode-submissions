class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s.islower() and t.islower():
            if sorted(s) == sorted(t):
                return True
            else:
                return False
        else:
            return False
obj = Solution()
print(obj.isAnagram("racecar","carrace"))
