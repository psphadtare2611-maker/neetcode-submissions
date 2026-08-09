# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, node: Optional[TreeNode]) -> List[List[int]]:
        if node is None:
            return []

        result = []
        queue = deque([node])

        while queue:
            level = []

            # Number of nodes at current level
            for _ in range(len(queue)):
                e = queue.popleft()

                level.append(e.val)

                if e.left is not None:
                    queue.append(e.left)

                if e.right is not None:
                    queue.append(e.right)

            result.append(level)

        return result