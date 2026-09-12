class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        for right in range(len(s)):
            while s[right] in s[left:right]:
                left += 1
            length = right - left + 1
            max_length = max(max_length,length)

        return max_length


    