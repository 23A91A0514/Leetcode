from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)  # step 1: count frequencies
        for i, ch in enumerate(s):  # step 2: check each char in order
            if freq[ch] == 1:
                return i
        return -1  # step 3: no unique character
