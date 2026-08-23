# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.result = []
        def traverse(node):
            if not node: 
                self.result.append('N')   
                return
            self.result.append(str(node.val))
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return ','.join(self.result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        self.i = 0

        def build():
            if vals[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(vals[self.i])
            self.i += 1
            node.left = build()
            node.right = build()
            return node
        return build()
            