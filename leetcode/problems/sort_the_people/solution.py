class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [a[0] for a in sorted(list(zip(names, heights)), key=lambda a:a[1], reverse=True)]
        