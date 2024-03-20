class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            char = sorted(list(s))[0]
            return s.count(char)
        
        words = sorted([f(s) for s in words])

        def search(n):
            l, r = 0, len(words)
            while l < r:
                mid = (l + r) // 2
                if words[mid] > n:
                    r = mid
                else:
                    l = mid + 1
            return len(words) - l
        
        return [search(f(s)) for s in queries]

        
