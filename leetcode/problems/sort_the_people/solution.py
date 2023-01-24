class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [row[0] for row in sorted(map(list, zip(names, heights)), key=lambda a:a[1], reverse=True)]