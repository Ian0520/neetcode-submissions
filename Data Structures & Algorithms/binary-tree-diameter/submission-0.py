# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter if traverse through the node = left_depth + right_depth
        self.best = 0
        def find_depth(node):
            if not node:
                return 0
            left_depth = find_depth(node.left)
            right_depth = find_depth(node.right)
            self.best = max(self.best, left_depth+right_depth)
            return max(left_depth, right_depth) + 1
        find_depth(root)
        return self.best