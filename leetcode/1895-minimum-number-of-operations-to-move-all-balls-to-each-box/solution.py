class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes)

        left_balls = 0
        left_moves = 0
        right_balls = 0
        right_moves = 0

        for i in range(len(boxes)):

            answer[i] += left_moves
            left_balls += int(boxes[i])
            left_moves += left_balls

            j = len(boxes) - 1 - i
            answer[j] += right_moves
            right_balls += int(boxes[j])
            right_moves += right_balls

        return answer
        
