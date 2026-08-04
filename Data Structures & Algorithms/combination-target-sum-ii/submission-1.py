class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, total, subset):
            if total == target:
                result.append(subset.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                subset.append(candidates[i])
                backtrack(i + 1, total + candidates[i], subset)
                subset.pop()

        backtrack(0, 0, [])
        return result