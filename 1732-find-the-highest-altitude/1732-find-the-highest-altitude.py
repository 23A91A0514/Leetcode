class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        l=[0]
        for i in range(len(gain)):
            alt+=gain[i]
            l.append(alt)
        return max(l)

        