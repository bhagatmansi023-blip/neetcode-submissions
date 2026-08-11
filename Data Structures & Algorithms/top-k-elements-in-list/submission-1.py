class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num,freq in dic.items():
            bucket[freq].append(num)

        res = []
        for freq in range(len(nums),0,-1):
            for num in bucket[freq]:
                res.append(num)

                if len(res) == k:
                    return res