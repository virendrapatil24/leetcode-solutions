class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        return max([len(s1) * len(s2) for s1, s2 in combinations(words, 2)  if not (set(s1) & set(s2))], default=0)
                    
                        
                        