class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        def backtrack(idx, val, last_operand, s):
            if idx == len(num):
                if val == target:
                    res.append(s)
                return

            for i in range(idx, len(num)):
                if num[idx] == "0" and i > idx:
                    break

                curr_num = int(num[idx: i + 1])

                if idx == 0:
                    backtrack(i + 1, curr_num, curr_num, str(curr_num))
                else:
                    backtrack(i + 1, val + curr_num, curr_num, s + "+" + str(curr_num))
                    backtrack(i + 1, val - curr_num, -curr_num, s + "-" + str(curr_num))
                    backtrack(i + 1, val - last_operand + (last_operand * curr_num), last_operand * curr_num, s + "*" + str(curr_num))

        backtrack(0, 0, 0, "")
        return res
        
