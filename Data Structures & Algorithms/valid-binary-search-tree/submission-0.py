# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, interval):
            if not node:
                return True
            if node.val >= interval[1] or node.val <= interval[0]:
                return False
            return (isValid(node.left, (interval[0], node.val)) and
                    isValid(node.right, (node.val, interval[1])))
        return isValid(root, (float("-inf"), float("inf")))