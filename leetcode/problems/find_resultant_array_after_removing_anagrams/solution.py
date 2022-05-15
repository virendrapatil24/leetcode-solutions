class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        while(i < len(words)):
            x = [a for a in words[i-1]]
            y = [b for b in words[i]]
            x.sort()
            y.sort()
            if  Counter(x) == Counter(y):
                words.remove(words[i])
            else:
                i += 1
        return words