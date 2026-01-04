class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        
        for n in nums:
            res = []
            c = 0
            
            j = 1
            while j * j <= n:
                if n % j == 0:
                    q = n // j
                    
                    if j == q:
                        c += 1
                        res.append(j)
                    else:
                        c += 2
                        res.append(j)
                        res.append(q)
                j += 1
            
            if c == 4:
                total += sum(res)
        
        return total
