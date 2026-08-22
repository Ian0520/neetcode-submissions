# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root, left, right
        # inorder: left, root, right
        # use root in preorder to decide inorder
        inorder_index = {
            val: i for i, val in enumerate(inorder)
        }
        preorder_i = 0

        # left, right -> range of inorder
        def build(left, right):
            nonlocal preorder_i

            if left > right:
                return None

            # preorder 的下一個一定是目前 subtree 的 root
            root_val = preorder[preorder_i]
            preorder_i += 1

            root = TreeNode(root_val)

            # 找 root 在 inorder 的位置
            mid = inorder_index[root_val]

            # preorder 順序是 root -> left -> right
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)