class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        for index in range(m , len(nums1)):
            nums1[index] = nums2[i]
            i += 1
        nums1.sort()