class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRobber(arr):
            prev2 = 0
            prev1 = 0
            for money in arr:
                curr = max(prev1, money+prev2)
                prev2 = prev1
                prev1= curr
            return prev1
        n = len(nums)
        if n == 1:
            return nums[0]
        case1 = houseRobber(nums[:-1])
        case2 = houseRobber(nums[1:])
        return max(case1, case2)