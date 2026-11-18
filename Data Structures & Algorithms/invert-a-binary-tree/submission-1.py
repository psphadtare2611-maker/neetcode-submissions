# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        queue = deque([root])
        while queue:
            e = queue.popleft()
            e.right,e.left = e.left,e.right
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
        return root