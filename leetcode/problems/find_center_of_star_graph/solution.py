class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x,y = edges[0][0], edges[0][1]
        if x==edges[1][0] or x == edges[1][1]:
            return x
        return y