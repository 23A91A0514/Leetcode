class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n + 10):
            s = 1
            temp = i
            
            while temp > 0:
                rev = temp % 10
                s = s * rev
                temp = temp // 10
                
            if s % t == 0:
                return i