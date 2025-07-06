from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # Traverse the digits from end to start
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If loop completes, it means we had all 9s, e.g. [9, 9, 9] -> [0, 0, 0]
        # So we need to insert 1 at the beginning
        return [1] + digits
