class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color_map = {}
        colors_set = {}
        res = []
        for x, y in queries:
            if x in ball_color_map:
                prev_y = ball_color_map[x]
                if colors_set[prev_y] == 1:
                    del colors_set[prev_y]
                else:
                    colors_set[prev_y] -= 1
                
            colors_set[y] = colors_set.get(y, 0) + 1
            ball_color_map[x] = y
            res.append(len(colors_set))
            # print(colors_set, ball_color_map)
        return res
        
