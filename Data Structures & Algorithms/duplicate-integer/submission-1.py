class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        result = []
        for i in range(0, n):
            if nums[i] in result:
                return True
            result.append(nums[i])
        return False