class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = ""

        for ch in str(n):
            if ch != '0':
                digits += ch

        if digits == "":
            return 0

        x = int(digits)
        digit_sum = sum(int(ch) for ch in digits)

        return x * digit_sum