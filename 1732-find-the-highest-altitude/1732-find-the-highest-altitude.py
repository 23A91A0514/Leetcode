class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        s=0
        l=[]
        for i in range(len(gain)):
            alt+=gain[i]
            s=max(alt,s)
        
        return s

        