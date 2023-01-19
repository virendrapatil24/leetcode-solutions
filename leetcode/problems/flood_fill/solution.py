class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        org_color = image[sr][sc]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] == color or  image[r][c] != org_color:
                return
            
            image[r][c] = color
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        dfs(sr,sc)

        return image