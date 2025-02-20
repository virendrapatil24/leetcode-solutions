class Solution:
    def myAtoi(self, s: str) -> int:
        value = ""
        is_neg = False
        is_first = False
        for char in s:
            if char == " " and not is_first:
                continue
            
            if char.isdigit():
                if not is_first:
                    is_first = True
                value += char
            elif char == "-" and not is_first:
                is_neg = True
                is_first = True
            elif char == "+" and not is_first:
                is_first = True
                continue
            else:
                break
        i = 0
        while i < len(value) and value[i] == "0":
            i += 1
        value = value[i:]
        value = int(value) if value else 0
        if is_neg: value *= -1

        if value < (2 ** 31) * -1:
            value = (2 ** 31) * -1
        
        if value > (2 ** 31) - 1:
            value = (2 ** 31) - 1

        return value
        
