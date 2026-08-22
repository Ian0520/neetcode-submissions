# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def traverse(node, path_max):
            if not node:
                return
            if node.val >= path_max:
                self.count += 1
            new_max = max(node.val, path_max)
            traverse(node.left, new_max)
            traverse(node.right, new_max)
            return 
        traverse(root, -101)
        return self.count