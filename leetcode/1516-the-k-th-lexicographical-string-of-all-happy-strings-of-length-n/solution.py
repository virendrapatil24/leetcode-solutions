class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []
        letters = ['a', 'b', 'c']
        def create_hs(temp):
            if len(temp) == n:
                happy_strings.append("".join(temp))
                return
        
            for i in range(3):
                if not temp or (temp and temp[-1] != letters[i]):
                    temp.append(letters[i])
                    create_hs(temp)
                    temp.pop()
        create_hs([])
        return happy_strings[k - 1] if k <= len(happy_strings) else ""

        
