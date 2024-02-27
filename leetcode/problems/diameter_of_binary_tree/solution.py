# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node, res):
            if not node:
                return 0
            left = height(node.left, res)
            right = height(node.right, res)
            res[0] = max(res[0], left + right)
            return max(left, right) + 1
        res = [0]
        height(root, res)
        return res[0]
        