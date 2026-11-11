class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        result = []

        for i in range(len(nums)):
            # 1. Remove indices out of window
            if dq and dq[0] == i - k:
                dq.popleft()

            # 2. Remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Store result (when window is formed)
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result