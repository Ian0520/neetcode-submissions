# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = queue.Queue()
        q.put((root,0))
        while not q.empty():
            node, depth = q.get()
            if not node: 
                continue
            if len(result) <= depth:
                result.append([node.val])
            else:
                result[depth].append(node.val)
            q.put((node.left, depth+1))
            q.put((node.right, depth+1))
        return result