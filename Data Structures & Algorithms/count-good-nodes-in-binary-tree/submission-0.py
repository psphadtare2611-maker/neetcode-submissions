# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_value):
            if node is None:
                return 0

            # Check if current node is good
            if node.val >= max_value:
                count = 1
            else:
                count = 0

            # Update maximum value seen so far
            max_value = max(max_value, node.val)

            # Check left and right subtree
            count += dfs(node.left, max_value)
            count += dfs(node.right, max_value)

            return count

        return dfs(root, root.val)
        