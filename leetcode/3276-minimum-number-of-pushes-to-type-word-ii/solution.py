class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_count = [0] * 26
        for char in word:
            letter_count[ord(char) - ord("a")] += 1
        
        letter_count.sort(reverse=True)

        total_key_presses = 0
        for idx, count in enumerate(letter_count):
            if count == 0:
                break
            total_key_presses += (idx // 8 + 1) * count

        return total_key_presses
        
