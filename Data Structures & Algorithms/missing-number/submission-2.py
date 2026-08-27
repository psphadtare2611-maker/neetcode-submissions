class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num = n
        expected = num*(num+1)//2
        actual = sum(nums)
        return expected - actual