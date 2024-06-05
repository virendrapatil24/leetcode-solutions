class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for char in set(words[0]):
            min_count = inf
            for word in words:
                curr_count = word.count(char)
                min_count = min(min_count, curr_count)
                if min_count == 0:
                    break
            res.extend([char] * min_count)

        return res
