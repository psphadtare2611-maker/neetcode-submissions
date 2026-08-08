# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, node):
        if node==None:
            return 0

        
        leftSum = self.solve(node.left)
        rightSum = self.solve(node.right)
        if leftSum < 0:
            leftSum = 0
        if rightSum < 0:
            rightSum = 0
        self.maxi = max(self.maxi, leftSum + node.val + rightSum)
        return max(leftSum, rightSum) + node.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float("-inf")
        self.solve(root)
        return self.maxi
        