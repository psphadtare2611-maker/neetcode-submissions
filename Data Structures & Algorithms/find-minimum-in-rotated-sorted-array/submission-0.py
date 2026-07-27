class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        min_num = float("inf")
        for i in range(0, n):
            min_num = min(min_num, nums[i])
        return min_num