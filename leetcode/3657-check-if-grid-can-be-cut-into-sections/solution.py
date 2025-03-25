class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [(r[0], r[2]) for r in rectangles]
        y = [(r[1], r[3]) for r in rectangles]

        x.sort()
        y.sort()

        def count_non_overlapping(intervals):
            count = 0
            prev = -1
            for interval in intervals:
                if interval[0] < prev:
                    prev = max(interval[1], prev)
                else:
                    count += 1
                    prev = interval[1]
            return count

        return max(count_non_overlapping(x), count_non_overlapping(y)) >= 3

        
