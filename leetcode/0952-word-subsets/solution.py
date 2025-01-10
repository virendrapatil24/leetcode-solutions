class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            counter = [0] * 26
            for char in word:
                counter[ord(char) - ord('a')] += 1
            return counter
        
        b_counter = [0] * 26
        for b_word in words2:
            for idx, cnt in enumerate(count(b_word)):
                b_counter[idx] = max(b_counter[idx], cnt)
        
        universal = []
        for a_word in words1:
            a_counter = count(a_word)
            is_universal = True
            for i in range(26):
                if b_counter[i] > a_counter[i]:
                    is_universal = False
                    break

            if is_universal: 
                universal.append(a_word)
        
        return universal

        
