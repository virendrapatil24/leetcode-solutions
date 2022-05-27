class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len = 0
        for i in sentences:
            x = len([ x for x in i.split()])
            max_len = max(max_len, x)
            
        return max_len
        