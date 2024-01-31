# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q, res = deque(), []
        q.append(root)
        while q:
            qlen, row = len(q), []
            for _ in range(qlen):
                node = q.popleft()
                row.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(row)

        return res


        