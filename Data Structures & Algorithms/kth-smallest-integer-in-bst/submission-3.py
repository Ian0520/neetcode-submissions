# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.sorted_nodes = []
        def traverse(node):
            if not node:
                return None
            traverse(node.left)
            self.sorted_nodes.append(node.val)
            traverse(node.right)
        traverse(root)
        print(self.sorted_nodes)
        return self.sorted_nodes[k-1]