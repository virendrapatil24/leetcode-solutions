# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        levels = []
        i = 0
        while i < n:
            
            depth = 1
            while i < n and traversal[i] == "-":
                depth += 1
                i += 1

            val = ""
            while i < n and traversal[i].isdigit():
                val += traversal[i]
                i += 1
            val = int(val)

            while levels and len(levels) > depth:
                levels.pop()
            
            node = TreeNode(val)
            if levels:
                if levels[-1].left == None:
                    levels[-1].left = node
                else:
                    levels[-1].right = node
            
            levels.append(node)
            i += 1
        
        return levels[0]
        


            
            
                
        
