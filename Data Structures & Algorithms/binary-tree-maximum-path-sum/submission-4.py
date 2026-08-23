# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")
        def traverse(node):
            if not node:
                return 0
            left_path = traverse(node.left)
            right_path = traverse(node.right)
            both_path = left_path + right_path + node.val
            best = max(left_path, right_path, 0) + node.val
            self.maxSum = max(both_path, self.maxSum, best)
            return best
        traverse(root)
        return self.maxSum
        