class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        mapAns = {}
        for i in range(len(matches)):
            if matches[i][0] in mapAns:
                mapAns[matches[i][0]][0] += 1
            else:
                mapAns[matches[i][0]] = [1, 0]
            if matches[i][1] in mapAns:
                mapAns[matches[i][1]][1] += 1
            else:
                mapAns[matches[i][1]] = [0, 1]
        ans1 = [k for k, v in mapAns.items() if v[1] == 0]
        ans2 = [k for k, v in mapAns.items() if v[1] == 1]
        return [sorted(ans1), sorted(ans2)]
