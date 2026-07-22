class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        s=0
        for i in range(0,n):
            l=start+2*i
            s^=l
        return s

        