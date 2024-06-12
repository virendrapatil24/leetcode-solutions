class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        score = 0
        labelsMap = {}
        for val, lab in sorted(zip(values, labels), reverse=True):
            if not numWanted:
                break
            
            if labelsMap.get(lab, 0) < useLimit:
                score += val
                labelsMap[lab] = labelsMap.get(lab, 0) + 1
                numWanted -= 1

        return score

