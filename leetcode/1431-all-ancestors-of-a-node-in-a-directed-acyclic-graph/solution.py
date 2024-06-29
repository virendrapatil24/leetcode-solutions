class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parent_to_kids = defaultdict(list)
        for parent, kid in edges:
            parent_to_kids[parent].append(kid)
        
        def dfs(ancestor, kid):
            if not (res[kid] and res[kid][-1] == ancestor):
                if kid != ancestor:
                    res[kid].append(ancestor)
                for grand_child in parent_to_kids[kid]:
                    dfs(ancestor, grand_child)
            return 

        res = [[] for _ in range(n)]
        for i in range(n):
            dfs(i, i)
        return res
