# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        post_idx_map = {}
        for i, val in enumerate(postorder):
            post_idx_map[val] = i
        
        def build(i1, i2, j1, j2):
            if i1 > i2 or j1 > j2:
                return None

            root = TreeNode(preorder[i1])
            if i1 != i2:
                left_val = preorder[i1 + 1]
                mid = post_idx_map[left_val]
                left_size = mid - j1 + 1
                root.left = build(i1 + 1, i1 + left_size, j1, mid)
                root.right = build(i1 + left_size + 1, i2, mid + 1, j2 - 1)

            return root
        
        return build(0, n - 1, 0, n - 1)

        
