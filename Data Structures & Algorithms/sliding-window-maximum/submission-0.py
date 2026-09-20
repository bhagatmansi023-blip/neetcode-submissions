class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):

            # 1. Remove indices that are outside the window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Window is ready when i >= k - 1
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result