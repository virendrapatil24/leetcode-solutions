class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = [0] * len(queries)
        prefix_sum = [0] * len(words)
        sum = 0
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                sum += 1
            prefix_sum[i] = sum

        for idx, query in enumerate(queries):
            res[idx] = prefix_sum[query[1]] - (0 if query[0] == 0 else prefix_sum[query[0] - 1])
        return res
        
