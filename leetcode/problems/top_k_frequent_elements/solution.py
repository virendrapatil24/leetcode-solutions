class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        y = x.most_common(k)
        ans = []
        for i in range(k):
            ans.append(y[i][0])
            
        return ans