class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalk_sum = sum(chalk)
        rem_chalk = k % chalk_sum
        for idx, stud in enumerate(chalk):
            rem_chalk -= stud
            if rem_chalk < 0:
                return idx
        return -1

        
