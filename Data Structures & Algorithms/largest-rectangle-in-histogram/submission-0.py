class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights) + 1):
            curr_height = heights[i] if i < len(heights) else 0

            while stack and heights[stack[-1]] > curr_height:
                height = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1

                area = height * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area
