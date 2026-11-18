class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        prev2 = 1
        prev = 1
        for _ in range(2,n+1):
            curr = prev+prev2
            prev2 = prev
            prev = curr
        return prev