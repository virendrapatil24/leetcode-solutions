class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s_list = (s1 + " " + s2).split(" ")
        s_map = {}
        for word in s_list:
            s_map[word] = s_map.get(word, 0) + 1
        res = []
        for k, v in s_map.items():
            if v == 1:
                res.append(k)
        return res
        
