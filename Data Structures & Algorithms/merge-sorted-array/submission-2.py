class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr = 0
        index = m
        while index < len(nums1):
            nums1[index] = nums2[ptr]
            ptr += 1
            index += 1
        nums1.sort()
        return nums1
         
        