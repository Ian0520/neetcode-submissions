# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append((root, 0))
        result = []
        while q:
            node, depth = q.popleft()
            if not node: 
                continue
            if len(result) <= depth:
                result.append(node.val)
            q.append((node.right, depth+1))
            q.append((node.left, depth+1))
        return result