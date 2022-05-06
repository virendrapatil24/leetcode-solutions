class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ans = set(ransomNote)
        
        for i in ans:
            if ransomNote.count(i) > magazine.count(i): return False
        
        return True