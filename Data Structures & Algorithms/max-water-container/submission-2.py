class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        res = 0
        while left <right:
            h = min(heights[left], heights[right])
            res = max(res, h * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res