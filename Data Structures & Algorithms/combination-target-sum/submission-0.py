class Solution:
    def combinationSum(self, nums: List[int], k: int) -> List[List[int]]:
        result = []
        def backtrack(index, total, subset):
            if total == k:
                result.append(subset.copy())
                return
            elif total > k:
                return
            if index >= len(nums):
                return
            subset.append(nums[index])
            Sum = total + nums[index]
            backtrack(index, Sum, subset)
            e = subset.pop()
            Sum -= e
            backtrack(index + 1, Sum, subset)
        backtrack(0, 0, [])
        return result