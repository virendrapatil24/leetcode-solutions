class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleastk(k):
            vowel = defaultdict(int)
            k_freq = 0
            count = 0
            l = 0
            for r in range(len(word)):
                if word[r] in 'aioue':
                    vowel[word[r]] += 1
                else:
                    k_freq += 1
                
                while len(vowel) == 5 and k_freq >= k:
                    count += len(word) - r
                    if word[l] in "aioue":
                        vowel[word[l]] -= 1
                    else:
                        k_freq -= 1
                    if vowel[word[l]] == 0:
                        vowel.pop(word[l])
                    l += 1
            return count
        return atleastk(k) - atleastk(k + 1)
