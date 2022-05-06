class Solution:
    def removeDuplicates(self, S: str, K: int) -> str:
        SC, st, i, j = list(S), [0], 1, 1
        while j < len(S):
            SC[i] = SC[j]
            if i == 0 or SC[i] != SC[i-1]: st.append(i)
            elif i - st[-1] + 1 == K: i = st.pop() - 1
            i += 1
            j += 1
        return "".join(SC[:i])
            