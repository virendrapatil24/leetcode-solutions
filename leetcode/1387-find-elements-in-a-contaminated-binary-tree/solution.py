# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.dfs(root, 0) 

    def find(self, target: int) -> bool:
        return target in self.seen

    def dfs(self, node, curr_val):
        if not node:
            return 
        self.seen.add(curr_val)
        self.dfs(node.left, curr_val * 2 + 1)
        self.dfs(node.right, curr_val * 2 + 2)
        
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
